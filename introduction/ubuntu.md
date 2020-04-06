# linux

パッケージの依存関係を解決するインストールコマンド
```bash
sudo apt install gdebi
sudo gdebi [パッケージ名]
```

ディレクトリを英語名に変換する
```bash
LANG=C xdg-user-dirs-gtk-update
```

スクリーンショットアプリはアクティビティから以下の単語を検索
```
gnome-screenshot
```

.bashrcに書く内容
```bash
# This code already exists in .bashrc. But, I modify a part.
if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;33m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
fi

export LANG=C.UTF-8
export LANGUAGE=en_US

alias py36="conda activate py36"
py36
```

