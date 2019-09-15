import os, sys
sys.path.append(os.path.dirname(__file__))

import numpy as np

import chainer
import chainer.functions as F
from chainer.backends import cuda

from chainercv import utils
from chainercv.utils.bbox.bbox_iou import bbox_iou
from chainercv.links.model.fpn.mask_utils import mask_to_segm
from chainercv.links.model.fpn.misc import smooth_l1

def converter1(batch, device=None):
    # do not send data to gpu (device is ignored)
    return tuple(list(v) for v in zip(*batch))

class TrainChain(chainer.Chain):

    def __init__(self, model):
        super(TrainChain, self).__init__()
        with self.init_scope():
            self.model = model

    def forward(self, imgs, gt):
        loss = 0
        chainer.reporter.report({
            'loss': loss,
            #'loss/rpn/loc': rpn_loc_loss, 'loss/rpn/conf': rpn_conf_loss,
        },self)
        return loss

