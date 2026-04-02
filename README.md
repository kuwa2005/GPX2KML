# GPX2KML 変換ツール（Fork版）

GPSログを国土地理院地図などで扱いやすいKMLに変換する、ブラウザ実行型ツールです。  
このForkはUI刷新と運用改善を含む改修版です。

## 現在のファイル構成

- `GPX2KML2.html` - 現行版（Tailwind UI）
- `README.md` - 本ドキュメント

## 使い方

1. `GPX2KML2.html` をブラウザで開きます
2. GPXファイルをドラッグ&ドロップ、またはファイル選択で読み込みます
3. 変換結果（KML）が画面に表示されます
4. 保存ボタンからダウンロードします

### ダウンロード仕様

- 単一ファイル入力: `.kml` を直接ダウンロード
- 複数ファイル入力: 変換済み `.kml` をまとめた `.zip` を1ファイルでダウンロード

## 主な機能

- GPXからKMLへの変換
- 複数ファイル一括変換（ZIP出力）
- GPX統計情報表示
  - トラック数
  - 総ポイント数
  - 総距離
  - 累積登り
- 標高プロファイル表示（距離×標高）
- ダーク/ライトモード切り替え
  - テーマはCookieに保存され、リロード後も復元

## 注意事項

- 現行版はCDNを利用しています（Tailwind/JSZip/Google Fonts）。
- そのため、通常はインターネット接続が必要です。
- オフライン版は別途作成予定です。

## ライセンス/クレジット

- Original work: [guchi999/GPX2KML](https://github.com/guchi999/GPX2KML)
- Modified version: [kuwa2005/GPX2KML](https://github.com/kuwa2005/GPX2KML)

