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
以下のコマンドを入力する、$image_nameにイメージの名前をつける。\$Dockerfile_nameにはイメージ化するdockerfileのファイル名を入れる。入れない場合はDockerfileが選択される。
```sh
docker build . -t=$image_name -f=$Dockerfile_name 
```
### 例
この例の場合、このフォルダ内にあるDockerfile内のARGによって宣言された変数へ値を埋め込む。そのために、ホスト側にはUSER_IDなどの変数が宣言されているものとする。
```sh
docker build . --build-arg USER_ID=$USER_ID --build-arg GROUP_1_ID=$GROUP_1_ID --shm-size=16g --tag=coder
```

## コンテナを作る
```sh
docker run -d -it --name $container_name $image_name
```
### 例
```sh
docker run -d -it --shm-size=16g -v $CODEBOX:/home/coder/codebox/ -v $DATABOX:/home/coder/databox/ --gpus all --name coder1 coder
```
```sh
docker run -d -it --shm-size=16g -v $CODEBOX:/home/coder/codebox/ -v $DATABOX:/home/coder/databox/ --gpus all --name coder2 coder-10.2
```

Note: -dはデーモン化、つまりつけっぱなしにする。-itはわすれた。--nameはコンテナ名

### ホストとデータ共有
runの時点で設定する必要あり
```sh
docker run -v [ホストディレクトリの絶対パス]:[コンテナの絶対パス] [イメージ名]
```
参考:[Yarimizu14, 【Docker】Dockerでホストのディレクトリをマウントする](https://qiita.com/Yarimizu14/items/52f4859027165a805630)

### 共有メモリ増設
これを使うことでpytorchのdataloaderのメモリ不足を回避できる。
```sh
docker run --shm-size=[数値][単位(G/M)] [イメージ名]
```

### GPUの使用
GPUを使用できるようになる。これは[nvidia](https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(Native-GPU-Support)#usage)のページを参照。
```sh
docker run --gpus all [イメージ名]
```

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
