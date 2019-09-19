import os, sys

import chainer
from chainer import Variable
from chainer import optimizers
from chainer import iterators

import numpy as np
import os
import cv2
from skimage import segmentation
from distutils.util import strtobool

from model.model import KanezakiNet
from exec_config import cmd_line_args
from dataset.xxx import xxx_extention_dataset

def main(args=None):
    # Arguments
    args = cmd_line_args(args)

    model = KanezakiNet(3,n_channel=args.n_channel,n_conv=args.n_conv)
    if(args.gpu >= 0):
        print('using gpu {}'.format(args.gpu))
        model.to_gpu(args.gpu)
    loss_fn = F.softmax_cross_entropy
    optimizer = optimizers.MomentumSGD(lr=args.learning_rate,momentum=0.9).setup(model)
    #xp = model.xp

    im = cv2.imread(args.input)
    data = Variable(np.array([im.transpose((2,0,1)).astype('float32')/255.]))
    
    labels = segmentation.slic(im, compactness=args.compactness, n_segments=args.n_superpixels)
    lables = labels.reshape(im.shape[0]*im.shape[1])
    u_labels = np.unique(labels)
    l_inds = []
    for i in range(len(u_labels)):
        l_inds.append(np.where(labels==u_labels[i])[0])
    
    label_colours = np.random.randint(255,size=(100,3))

if __name__ == "__main__":
    args=[
          "--input=/content/drive/My Drive/Colab Notebooks/unsupervised_segmentation_chainer/images/101027.jpg",
          "--use_colab=true",
          "--gpu=0",
    ]
    main(args=args)