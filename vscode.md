# Visual Studio Code (vscode)
## 拡張機能
導入するべき拡張機能たち
- vscode-icons  
    アイコン変更

- One Dark Pro  
    テーマ変更

- Python  
    python拡張

- C/C++  
    C/C++拡張

- Backet Pair Colorizer  
    括弧の対応環境を色で理解できる

- Markdown PDF  
    markdownのpdf化

- Markdown+Math  
    markdown環境でlatexの数式を描くための環境

- Live Server  
    HTML+javascriptの動作確認環境

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
```
{
    "workbench.startupEditor": "newUntitledFile",
    "workbench.iconTheme": "material-icon-theme",
    "workbench.colorTheme": "Material Theme High Contrast",
    "editor.minimap.enabled": false,
    "git.confirmSync": false,
    "workbench.editor.enablePreview": false,
    "editor.renderWhitespace": "all",
    "editor.wordWrap": "on",
    "editor.mouseWheelZoom": true,
    "workbench.colorCustomizations": {
    // 現在行の背景色を、エディタの背景色よりも暗いグレーに
        "editor.lineHighlightBackground": "#000000",
        // 行番号を水色に
        "editorLineNumber.foreground": "#0ff",
        // 空白文字を指定した色で表示
        "editorWhitespace.foreground": "#5e5e5e",
        // インデントガイドを赤で表示
        "editorIndentGuide.background": "#f00"
    }
}
```
