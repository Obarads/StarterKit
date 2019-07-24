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

## テーマの変更&各種設定
settings.jsonに以下の内容を貼り付け
```
{
    "workbench.colorTheme": "One Dark Pro",
    "workbench.iconTheme": "vscode-icons",
    "editor.minimap.enabled": false,
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
    }
}
```