# Anaconda (conda)
## 環境構築(基本的なライブラリをインストールする&python3.6)
```
conda create -n py36 python=3.6 anaconda
```

## 環境起動
```
source activate py36
```

## 環境から抜ける
```
source deactivate
```

## 環境削除
```
conda remove -n py36 --all
```
※削除できない場合は~anaconda3/envs/py36を直接削除する。

## その他
.bashrcに下のものを記すことで簡単に環境起動(ubuntu、記したのちにsourceで読み込み)
```
alias py36='source activate py36'
```
