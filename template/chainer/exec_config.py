import os, sys
#sys.path.append(os.path.dirname(__file__))

from distutils.util import strtobool
from chainerui.utils import save_args

def cmd_line_args(args=None):
    parser = argparse.ArgumentParser(description='train model')
    parser = model_args(parser)
    parser = train_args(parser)
    parser = test_args(parser)
    parser = env_args(parser)
    parser = temporary_args(parser)
    
    args = parser.parse_args(args=args)
    save_args(args, args.output_dir)

    return args

def model_args(parser):
    parser.add_argument('--gpu', '-g', type=int, default=-1)
    parser.add_argument('--use_bn', type=strtobool, default='true')
    parser.add_argument('--use_do', type=strtobool, default='false')
    parser.add_argument('--do_ratio',  type=float, default=0)
    parser.add_argument('--n_channel', type=int, default=100, help='number of channels')
    parser.add_argument('--n_conv', type=int, default=2, help='number of convolutional layers')
    parser.add_argument('--n_superpixels', type=int, default=10000, help='number of superpixels')
    parser.add_argument('--compactness', type=float, default=100, help='compactness of superpixels')
    parser.add_argument('--input', type=str, required=True, help='input image file name')
    return parser

def train_args(parser):
    parser.add_argument('--cpu', '-c', type=int, default=1)
    parser.add_argument('--batchsize', '-b', type=int, default=32)
    parser.add_argument('--learning_rate', '-lr', type=float, default=0.1)
    parser.add_argument('--min_labels', type=int, default=3, help='minimum number of labels')
    parser.add_argument('--epoch', '-e', type=int, default=1000)
    parser.add_argument('--seed', '-s', type=int, default=777)
    parser.add_argument('--save_model', type=str, default='model_ae.npz')
    return parser
    
def test_args(parser):
    return parser

def env_args(parser):
    parser.add_argument('--use_colab', type=strtobool, default='false', help='when you use colab')
    parser.add_argument('--use_visualize', type=strtobool, default='true', help='visualization flag')
    parser.add_argument('--output_dir', type=str, default='result')
    return parser

def temporary_args(parser):
    #parser.add_argument('--X', type=int, default=0, help='example')
    return parser
    
