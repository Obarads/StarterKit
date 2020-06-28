# Visual Studio Code (vscode)
## 拡張機能
- Shades of Purple: 紫デザイン
- vscode-icons: アイコン
- Python: python拡張
- Babel JavaScript: Reactのために使用
- Backet Pair Colorizer: 括弧の対応環境を色で理解できる
- Markdown All in One: markdown記述が楽になる
- Live Server: HTML+javascriptの動作確認環境
- vim: vim風の操作が可能
- Docker: 環境構築用
- Live Share: vscodeに対する遠隔操作が可能
- Remote系: dockerにつなぐため

## 管理スペースが大きいという警告がある場合(only ubuntu)
「Unable to watch for file changes in this large workspace. Please follow the instructions link to resolve this issue.(Visual Studio Code はこの大規模なワークスペース内のファイル変更を監視できません。この問題を解決するには、リンクの手順に従ってください。)」が出た場合、以下の内容を/etc/sysctl.confに追加、その後`sudo sysctl -p`を実行する。

```
fs.inotify.max_user_watches=524288
```

現在のメモリを確認するには、以下のコマンドを実行する。

```
cat /proc/sys/fs/inotify/max_user_watches
```

## windowsのvscodeのターミナルでanaconda prompt(Powershell版)を利用
- 以下の内容をsetting.jsonに追加する。
  - Hogeの箇所を自分の環境にあったものに変換すること。
- 以下の内容は、[_mekiさんの方法](https://qiita.com/_meki/items/5b4f06318f1a0986c55c)を参考にして作ったもの。
```json
"terminal.integrated.shellArgs.windows": [
    "-ExecutionPolicy", 
    "ByPass",
    "-NoExit",
    "-Command",
    "& 'C:\\Users\\Hoge\\AppData\\Local\\Continuum\\anaconda3\\shell\\condabin\\conda-hook.ps1'; conda activate 'C:\\Users\\Hoge\\AppData\\Local\\Continuum\\anaconda3'"
],
```

## テーマの変更&各種設定
settings.jsonに以下の内容を貼り付け
```json
{
    // Terminal
    "terminal.integrated.inheritEnv": false,
    "terminal.integrated.shell.linux": "/bin/bash",
    "terminal.integrated.shell.windows": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe", 
    // Workbench
    "workbench.editor.enablePreview": false,
    "workbench.startupEditor": "newUntitledFile",
    "workbench.iconTheme": "vscode-icons",
    "workbench.colorTheme": "Shades of Purple",
    "workbench.colorCustomizations": {
        "editor.lineHighlightBackground": "#000000",
        "editorLineNumber.foreground": "#0ff",
        "editorWhitespace.foreground": "#5e5e5e",
        "editorIndentGuide.background": "#f00",
        "tab.activeBackground": "#613c85",
        "tab.activeForeground": "#fff",
        "tab.unfocusedActiveBackground": "#191038",
        "statusBar.background": "#b01a31",
        "statusBar.noFolderBackground": "#b01a31",
        "statusBar.noFolderForeground": "#fff",
        "statusBar.debuggingBackground": "#b01a31",
        "statusBar.debuggingForeground": "#fff",
        "statusBar.foreground": "#ffffff"
    },
    // Window
    "window.zoomLevel": 0,
    // Git
    "git.confirmSync": false,
    // Editor
    "editor.multiCursorModifier": "ctrlCmd",
    "editor.minimap.enabled": false,
    "editor.lineNumbers": "relative",
    "editor.renderWhitespace": "all",
    "editor.mouseWheelZoom": true,
    "editor.wordWrap": "on",
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
    },
    // Extensions
    // live Server setting
    "liveServer.settings.donotVerifyTags": true,
    "liveServer.settings.donotShowInfoMsg": true,
    // VIM setting
    "vim.useSystemClipboard": true,
    "vim.hlsearch": true,
    "vim.visualstar": true,
    "vim.easymotion": true,
    "vim.leader": "<space>",
    "vim.easymotionKeys": "sdfghjkl",
    "vim.whichwrap": "h,l,<,>,[,]",
    "vim.useCtrlKeys": true,
    "vim.normalModeKeyBindingsNonRecursive": [
        { // sync vim undo with vscode undo
            "before": [
                "u"
            ],
            "after": [],
            "commands": [
                {
                    "command": "undo"
                }
            ]
        },
        { // sync vim redo with vscode redo
            "before": [
                "<C-r>"
            ],
            "after": [],
            "commands": [
                {
                    "command": "redo"
                }
            ]
        },
        { // input enter on normal mode.
            "before": [
                "<Enter>"
            ],
            "after": [],
            "commands": [
                "editor.action.insertLineAfter"
            ]
        },
        { // input indent
            "before": [
                "<Tab>"
            ],
            "after": [],
            "commands": [
                "editor.action.indentLines"
            ]
        },
        { // input outdent
            "before": [
            ],
            "after": [],
            "commands": [
                "editor.action.outdentLines"
            ]
        }
    ],
    "vim.statusBarColorControl": true,
    "vim.statusBarColors.normal": [
        "#0050c7",
        "#ffffff"
    ],
    "vim.statusBarColors.insert": [
        "#176332",
        "#ffffff"
    ],
    "vim.statusBarColors.visual": [
        "#b01a31",
        "#ffffff"
    ],
    "vim.statusBarColors.visualline": [
        "#b01a31",
        "#ffffff"
    ],
    "vim.statusBarColors.visualblock": [
        "#b01a31",
        "#ffffff"
    ],
    "vim.statusBarColors.replace": [
        "#E2A478",
        "#161821"
    ],
    "vim.statusBarColors.commandlineinprogress": [
        "#285366",
        "#ffffff"
    ],
    "vim.statusBarColors.searchinprogressmode": [
        "#572e85",
        "#ffffff"
    ],
    "vim.statusBarColors.easymotionmode": [
        "#fcff3b",
        "#1c1c1c"
    ],
    "vim.statusBarColors.easymotioninputmode": [
        "#ffbb3d",
        "#161821"
    ],
    "vim.statusBarColors.surroundinputmode": [
        "#818596",
        "#161821"
    ]
}
```

## vim用のキーコンフィグ
```json
// Place your key bindings in this file to override the defaults
[
    {// move between editors
        "key": "ctrl+h",
        "command": "workbench.action.previousEditor"
    },
    {// move between editors
        "key": "ctrl+l",
        "command": "workbench.action.nextEditor"
    },
    {// move between editor and terminal
        "key": "ctrl+k",
        "command": "workbench.action.terminal.toggleTerminal",
        "when": "editorTextFocus"
    },
    {// move between editor and terminal
        "key": "ctrl+k",
        "command": "workbench.action.focusActiveEditorGroup",
        "when": "terminalFocus"
    },
    {// move between editor and sidebar
        "key": "ctrl+j",
        "command": "workbench.action.focusSideBar",
        "when": "editorTextFocus"
    },
    {// move between editor and sidebar
        "key": "ctrl+j",
        "command": "workbench.action.focusActiveEditorGroup",
        "when": "sideBarFocus"
    }
]
```



## 拡張機能の作成について
publisherの作成済みなら、以下のコマンドをすることで拡張機能生成可能。この場合、ローカル環境に生成されるだけで、オンラインにはpublishされない。
```sh
vsce package
```
このあと、vscodeの拡張機能一覧の上にある点横3つのアイコンから install from VSIXを選択して、生成されたものを選択するだけ。  
もし、公開する場合は以下のようにする。バージョンを上げる場合は引数として、`minor`をつけるだけ。
```sh
vsce publish
```