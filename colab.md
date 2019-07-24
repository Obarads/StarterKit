# Colaboratory (colab)
## GPUの設定
編集 -> ノートブックの設定でハードウェアアクセラレータはGPUにする。
- GPUの確認コマンド
```
import tensorflow as tf
tf.test.gpu_device_name()
```

## Chainerのインストール
cudaに関してはとりあえず最新(12/9時点)のものを利用。chainerexとchainer-chemistryは任意。
```
!git clone https://github.com/Obarads/chainer-pointnet-autoencoder.git
!pip install chainer
!git clone https://github.com/corochann/chainerex.git
!pip install -e chainerex
!git clone https://github.com/pfnet-research/chainer-chemistry.git
!pip install -e chainer-chemistry
!pip install cupy-cuda92
```