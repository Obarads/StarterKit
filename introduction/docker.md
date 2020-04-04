# Docker

導入のための公式サイト(nvidia-dockerも含む)
- [Get Docker Engine - Community for Ubuntu | Docker Documentation](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-repository)
- [Home · NVIDIA/nvidia-docker Wiki](https://github.com/NVIDIA/nvidia-docker/wiki)

これが終わった後に、dockerを起動する。

## 単語集
- コンテナ: 大雑把に言えば、仮想環境みたいなもの。
- イメージ: コンテナを作成するための大本のファイル。このファイルはvmwareとかで言うisoみたいなもの。Dockerfileをdocker buildすることで、このイメージを作成することができる。
- Dockerfile: 構築したい環境をDockerfileに書き込んでイメージすることができる。この変換をdocker buildという。

## 初心者の順序
1. ビルドする(飛ばしてもいい)
   1. Dockerfileを書く
   2. docker buildする
2. コンテナを作る
3. コンテナを起動したり止めたりそれにログインしたりする。

## ビルドする
以下のコマンドを入力する、$image_nameにイメージの名前をつける。
```sh
docker build . -t $image_name
```

## コンテナを作る
```sh
docker run -d -it --name $container_name $image_name
```
### 例
```sh
docker run -d -it --name tcx --gpus all nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04
```

Note: -dはデーモン化、つまりつけっぱなしにする。-itはわすれた。

### ホストとデータ共有する場合
runの時点で設定する必要あり
```sh
docker run -v [ホストディレクトリの絶対パス]:[コンテナの絶対パス] [イメージ名] [コマンド]
```
参考:[Yarimizu14, 【Docker】Dockerでホストのディレクトリをマウントする](https://qiita.com/Yarimizu14/items/52f4859027165a805630)

## コンテナを起動したり止めたりそれにログインしたりする。
スタート(起動)
```sh
docker start $container_name
```

ストップ(終了)
```sh
docker stop $container_name
```

ログイン
```sh
docker attach $container_name
```
