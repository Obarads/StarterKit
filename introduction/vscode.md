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

## テーマの変更&各種設定
settings.jsonに以下の内容を貼り付け
```json
{
    "workbench.iconTheme": "vscode-icons",
    "workbench.colorTheme": "Shades of Purple",
    "editor.multiCursorModifier": "ctrlCmd",
    "editor.minimap.enabled": false,
    "editor.lineNumbers": "relative",
    "liveServer.settings.donotVerifyTags": true,
    "liveServer.settings.donotShowInfoMsg": true,
    "workbench.startupEditor": "newUntitledFile",
    "git.confirmSync": false,
    "workbench.editor.enablePreview": false,
    "editor.renderWhitespace": "all",
    "workbench.colorCustomizations": {
        "editor.lineHighlightBackground": "#000000",
        "editorLineNumber.foreground": "#0ff",
        "editorWhitespace.foreground": "#5e5e5e",
        "editorIndentGuide.background": "#f00",
        "statusBar.background": "#b01a31",
        "statusBar.noFolderBackground": "#b01a31",
        "statusBar.debuggingBackground": "#b01a31",
        "statusBar.foreground": "#ffffff"
    },
    "window.zoomLevel": 0,
    "editor.mouseWheelZoom": true,
    "editor.wordWrap": "on",
    //"python.linting.pylintArgs": ["--generated-members=torch.*"],
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
    ],
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
    },
    "terminal.integrated.shell.linux": "/bin/bash",
    "cmake.configureOnOpen": false
}
```

## Debug example
```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "args": [
                "--load_config=configs/hoge.yaml",
                "--dataset_path=/hoge/dataset"
            ]
        }
    ]
}
```