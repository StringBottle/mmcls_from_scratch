import warnings

import matplotlib.pyplot as plt
import mmcv
import numpy as np
import torch

from mmcv.parallel import collate, scatter
from mmcv.runner import load_checkpoint

from mmcls.datasets.pipelines import Compose
from mmcls.models import build_classifier

def init_model():
    """
    Initialize a classifier from a config file.

    Args :
        config (str or :obj:'mmcv.Config') : Config file path or the config object

        checkpoint (str, optional) : Checkpoint path. If left as None, the model will not load any weights.


    Returns:
        nn.Module : The constructed classifier.

    """



def inference_model():


def show_result_pyplot():

