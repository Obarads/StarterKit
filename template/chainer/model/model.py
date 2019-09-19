import os, sys
sys.path.append(os.path.dirname(__file__))

import chainer
import chainer.functions as F
import chainer.links as L
from chainer import Sequential

class KanezakiNet(chainer.Chain):
    def __init__(self, input_dim, n_channel=100, n_conv=2):
        super(KanezakiNet, self).__init__()
        with self.init_scope():
            seq_model = Sequential()
            seq_model += Sequential(
                L.Convolution2D(input_dim, n_channel, ksize=3, stride=1, pad=1),
                F.relu,
                L.BatchNormalization(n_channel)
            )
            for _ in range(n_conv):
                seq_model += Sequential(
                    L.Convolution2D(n_channel,n_channel,ksize=3,stride=1,pad=1),
                    F.relu,
                    L.BatchNormalization(n_channel)
                )
            seq_model += Sequential(
                L.Convolution2D(n_channel,n_channel,ksize=1,stride=1,pad=0),
                L.BatchNormalization(n_channel)
            )

            self.seq_model = seq_model

    def __call__(self,x):
        return self.seq_model(x)
