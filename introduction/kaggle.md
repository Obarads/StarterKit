# Kaggle
## 準備
### Kaggle用の環境構築
- dockerを予めインストールしておく。
- [Kaggleのdocker](https://github.com/Kaggle/docker-python)をインストールする。以下のコマンドは2020年12月時点のもの。
  ```sh
  docker pull gcr.io/kaggle-gpu-images/python
  ```
- docker runする。これにより、k1コンテナが作成される。
  ```sh
  docker run -dit --shm-size=16g -v $CODEBOX:/mnt/codebox/ -v $DATABOX:/mnt/databox/ --gpus all -p 8888:8888 --name k1 gcr.io/kaggle-gpu-images/python:latest
  ```
- k1コンテナ内で、このレポジトリのcreate_user.shを動かす。ファイル権限問題を回避するために、dockerを動かしているアカウントのユーザーIDとグループIDを取る。
  ```
  sh create_user.sh [ユーザーID] [グループID]
  ```

