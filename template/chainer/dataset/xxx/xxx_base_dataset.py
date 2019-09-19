import os, sys

from os.path import join as pjoin
import h5py, csv, json
import numpy as np
import PIL

import chainer
from chainercv import utils
from chainercv.links.model.fpn.misc import scale_img
from chainercv import transforms

#chainer.config.cv_resize_backend = "cv2"

XXX_LABEL_NAMES = ()

class XxxBaseDataset(chainer.dataset.DatasetMixin):
    def __init__(self, debug=False):
        self.length = 0
        self.debug = debug
        pass

    def __len__(self):
        pass
        return self.length

    def get_example(self, idx):
        if self.debug:
            debug_param = {}
            debug_param["greeting"] ="Hello world."
            self.debug_print(debug_param)
        return idx

    def debug_print(self,debug_param):
        for param_key in debug_param.keys():
            print(param_key,":",debug_param[param_key])
        print("")#改行用

def get_file_path(data_path,folder_name,category_name,img_path,file_extention):
    dir_path = os.path.join(data_path,folder_name,category_name)
    file_number = img_path.split("/")[-1].split(".")[0]
    file_path = os.path.join(dir_path, file_number + "." +file_extention)
    return file_path

