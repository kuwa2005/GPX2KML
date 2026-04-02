"""Generate 1200x630 og-image.png for OGP (requires Pillow)."""
from __future__ import annotations

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "og-image.png"
W, H = 1200, 630


def pick_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    windir = os.environ.get("WINDIR", r"C:\Windows")
    candidates = [
        Path(windir) / "Fonts" / "meiryo.ttc",
        Path(windir) / "Fonts" / "YuGothR.ttc",
        Path(windir) / "Fonts" / "YuGothM.ttc",
        Path(windir) / "Fonts" / "msgothic.ttc",
    ]
    for p in candidates:
        if p.is_file():
            try:
                return ImageFont.truetype(str(p), size=size, index=0)
            except OSError:
                continue
    return ImageFont.load_default()


def main() -> None:
    img = Image.new("RGB", (W, H))
    px = img.load()
    c0 = (15, 23, 42)
    c1 = (2, 6, 23)
    for y in range(H):
        t = y / max(H - 1, 1)
        r = int(c0[0] + (c1[0] - c0[0]) * t)
        g = int(c0[1] + (c1[1] - c0[1]) * t)
        b = int(c0[2] + (c1[2] - c0[2]) * t)
        for x in range(W):
            px[x, y] = (r, g, b)

    draw = ImageDraw.Draw(img, "RGBA")

    # Soft glow orbs
    for cx, cy, rad, col in [
        (180, 120, 200, (34, 211, 238, 35)),
        (980, 480, 240, (52, 211, 153, 28)),
        (1020, 140, 160, (139, 92, 246, 22)),
    ]:
        for r in range(rad, 0, -3):
            a = int(col[3] * (r / rad) ** 2)
            bbox = (cx - r, cy - r, cx + r, cy + r)
            draw.ellipse(bbox, fill=(col[0], col[1], col[2], min(255, a)))

    # Simplified map grid
    grid = (30, 44, 67, 80)
    for x in range(0, W, 48):
        draw.line([(x, 0), (x, H)], fill=grid, width=1)
    for y in range(0, H, 48):
        draw.line([(0, y), (W, y)], fill=grid, width=1)

    # Route polyline (cyan)
    route = [
        (720, 480),
        (780, 360),
        (860, 320),
        (940, 200),
        (1020, 160),
        (1100, 220),
        (1140, 380),
    ]
    draw.line(route, fill=(34, 211, 238), width=8, joint="curve")
    for (x, y) in (route[0], route[-1]):
        r = 10
        draw.ellipse((x - r, y - r, x + r, y + r), fill=(52, 211, 153), outline=(236, 254, 255), width=2)

    title_font = pick_font(86)
    sub_font = pick_font(34)
    badge_font = pick_font(26)

    title = "GPX2KML"
    subtitle = "GPX → KML ブラウザ変換ツール"
    draw.text((72, 160), title, font=title_font, fill=(248, 250, 252))
    draw.text((72, 275), subtitle, font=sub_font, fill=(203, 213, 225))

    mono = pick_font(28)
    draw.text((72, 360), "単一: .kml 保存  ·  複数: .zip 一括", font=mono, fill=(148, 163, 184))

    # Badge
    bx0, by0, bx1, by1 = 72, 440, 280, 498
    draw.rounded_rectangle((bx0, by0, bx1, by1), radius=14, fill=(6, 78, 59, 230), outline=(45, 212, 191, 200), width=2)
    draw.text((96, 454), "ZIP一括対応", font=badge_font, fill=(236, 253, 245))

    img.convert("RGB").save(OUT, format="PNG", optimize=True)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
