# Kaggle
## 準備
### Kaggle用の環境構築
- できること: kaggleコンペに必要な環境をdocker上で扱えるようになる。
- dockerを予めインストールしておく。
- [Kaggleのdocker](https://github.com/Kaggle/docker-python)をインストールする。以下のコマンドは2020年12月時点のもの。
  ```sh
  docker pull gcr.io/kaggle-gpu-images/python
  ```
- docker runする。これにより、k1コンテナが作成される。
  ```sh
  docker run -dit --shm-size=16g -v $CODEBOX:/mnt/codebox/ -v $DATABOX:/mnt/databox/ --gpus all -p 8888:8888 --name k1 gcr.io/kaggle-gpu-images/python:latest
  ```
- k1コンテナ内で、このレポジトリの`introduction/docker/create_user.sh`を動かす。ファイル権限問題を回避するために、dockerを動かしているアカウントのユーザーIDとグループIDを取る。
  ```sh
  sh create_user.sh [ユーザーID] [グループID]
  ```

### kaggle.jsonの追加
- できること: kaggleコマンドが使えるようになる。
- `kaggle.json`を入手して`~/.kaggle`フォルダに入れる。
  - kaggle.jsonはアカウントページのAPI欄から入手可能。
- `Warning: Your Kaggle API key is readable by other users on this system! To fix this, you can run 'chmod 600 /home/coder/.kaggle/kaggle.json'`が出る場合は、エラーに従う。
  - ```sh
    chmod 600 /home/coder/.kaggle/kaggle.json
    ```

## コンペ開始
### コンペを始める
- わかること: コンペの出だし
- データセットをダウンロードする。以下の例ではコンペは[キャッサバコンペ](https://www.kaggle.com/c/cassava-leaf-disease-classification/overview)を扱う。
  ```sh
  kaggle competitions download -c cassava-leaf-disease-classification -p /home/coder/databox/Kaggle/cassava_leaf_disease_classification
  ```
  - -p: zipファイルのダウンロード先
- unzipする。
  ```
  unzip cassava-leaf-disease-classification.zip
  ```

### コードを書く。
- コードを書こう。