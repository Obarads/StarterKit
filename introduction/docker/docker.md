# Docker
- 導入のための公式サイト(nvidia-dockerも含む)
  - [Get Docker Engine - Community for Ubuntu | Docker Documentation](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-repository)
  - [Home · NVIDIA/nvidia-docker Wiki](https://github.com/NVIDIA/nvidia-docker/wiki)
- これが終わった後に、dockerを起動する。

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
### 概要
- 以下は特に何も設定しない場合のコマンドである。同ディレクトリにあるDockerfileを使う。
  ```sh
  docker build . 
  ```
### 普段使う例
- この例の場合、このフォルダ内にあるDockerfile内のARGによって宣言された変数へ値を埋め込む。そのために、ホスト側にはUSER_IDなどの変数が宣言されているものとする(これをする理由は、rootによる共有先のファイルのアクセス制限を回避するため)。
  - ちなみに、USER_IDは`id`コマンドで確認できる。
- `$image_name`は作成するイメージ名、`$Dockerfile_name`は指定したDockerfile名を入れる(つまり選択できる)ことで動作する。
  ```sh
  docker build . --build-arg UID=$USER_ID --build-arg GID=$GROUP_ID --shm-size=16g -t=$image_name:$version -f=Dockerfile
  ```

## コンテナを作って動作させる
### 概要
- dockerで最も使われるであろうコマンドが`docker run`。これによってdockerコンテナを作成後、動作する。
  ```sh
  docker run -it --name $container_name $image_name
  ```

## docker runのコマンド引数集
### ホストとデータ共有
- runの時点で設定する必要あり
  ```sh
  docker run -v [ホストディレクトリの絶対パス]:[コンテナの絶対パス] [イメージ名]
  ```
  参考:[Yarimizu14, 【Docker】Dockerでホストのディレクトリをマウントする](https://qiita.com/Yarimizu14/items/52f4859027165a805630)
### 共有メモリ増設
- これを使うことでpytorchのdataloaderのメモリ不足を回避できる。
  ```sh
  docker run --shm-size=[数値][単位(G/M)] [イメージ名]
  ```
### GPUの使用
- GPUを使用できるようになる。これは[nvidia](https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(Native-GPU-Support)#usage)のページを参照。
  ```sh
  docker run --gpus all [イメージ名]
  ```
### 普段使う例
- ```sh
  docker run -dit --shm-size=16g -v $CODEPATH:/home/coder/workspace/code/ -v $DATAPATH2:/home/coder/workspace/data2/ -v $DATAPATH1:/home/coder/workspace/data1/ --gpus all -p 8888:8888 --name c11.1 c-11.1
  ```
### Note
- -dはデーモン化、つまりつけっぱなしにする。-itはわすれた。--nameはコンテナ名

## コンテナを起動したり止めたりそれにログインしたりする。
- スタート(起動)
  ```sh
  docker start $container_name
  ```
- ストップ(終了)
  ```sh
  docker stop $container_name
  ```
- ログイン (おすすめ)
  ```sh
  docker exec -it [コンテナ名] /bin/bash
  ```
- ログイン
  ```sh
  docker attach $container_name
  ```

