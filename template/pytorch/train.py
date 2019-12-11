import os, sys

import torch

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

    

if __name__ == "__main__":
    main()