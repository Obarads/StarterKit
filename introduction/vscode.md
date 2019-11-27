# Visual Studio Code (vscode)
## 拡張機能
- Shades of Purple: 紫デザイン
- vscode-icons: アイコン
- Python: python拡張
- Babel JavaScript: Reactのために使用
- Backet Pair Colorizer: 括弧の対応環境を色で理解できる
- Markdown+Math: markdown環境でlatexの数式を描くための環境
- Live Server: HTML+javascriptの動作確認環境
- vim: vim風に編集できる

## 管理スペースが大きいという警告がある場合(only ubuntu)
「Unable to watch for file changes in this large workspace. Please follow the instructions link to resolve this issue.(Visual Studio Code はこの大規模なワークスペース内のファイル変更を監視できません。この問題を解決するには、リンクの手順に従ってください。)」が出た場合、以下の内容を/etc/sysctl.confに追加、その後`sudo sysctl -p`を実行する。

```
fs.inotify.max_user_watches=524288
```

現在のメモリを確認するには、以下のコマンドを実行する。

```
cat /proc/sys/fs/inotify/max_user_watches
```

## テーマの変更&各種設定
settings.jsonに以下の内容を貼り付け
```json
{
    "workbench.iconTheme": "vscode-icons",
    "editor.multiCursorModifier": "ctrlCmd",
    "editor.minimap.enabled": false,
    "liveServer.settings.donotVerifyTags": true,
    "liveServer.settings.donotShowInfoMsg": true,
    "workbench.startupEditor": "newUntitledFile",
    "git.confirmSync": false,
    "workbench.editor.enablePreview": false,
    "editor.renderWhitespace": "all",
    "workbench.colorCustomizations": {
        // 現在行の背景色を、エディタの背景色よりも暗いグレーに
        "editor.lineHighlightBackground": "#000000",
        // 行番号を水色に
        "editorLineNumber.foreground": "#0ff",
        // 空白文字を指定した色で表示
        "editorWhitespace.foreground": "#5e5e5e",
        // インデントガイドを赤で表示
        "editorIndentGuide.background": "#f00"
    },
    "window.zoomLevel": 0,
    "editor.mouseWheelZoom": true,
    "editor.wordWrap": "on",
    // VIM setting
    "vim.useSystemClipboard": true,
    "vim.hlsearch": true,
    "vim.visualstar": true,
    "vim.easymotion": true,
    "vim.leader": "<space>",
    "vim.whichwrap": "h,l,<,>,[,]",
    "vim.useCtrlKeys": true,
    "workbench.colorTheme": "Shades of Purple",
    "terminal.integrated.inheritEnv": false,
    "editor.tokenColorCustomizations": {
        "textMateRules": [
            {
                "name": "[MARKDOWN] - Color for Punctuation — Heading, `Code` and fenced ```code blocks```, **Bold**",
                "scope": [
                    "punctuation.definition.markdown",
                    "punctuation.definition.raw.markdown",
                    "punctuation.definition.heading.markdown",
                    "punctuation.definition.bold.markdown",
                    "punctuation.definition.italic.markdown"
                ],
                "settings": {
                    "foreground": "#ff5da0"
                }
            }
        ]
    }
}
```