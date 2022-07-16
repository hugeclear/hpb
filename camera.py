import numpy as np
from tqdm import tqdm
from PIL import Image

import torch.nn as nn
from torch.autograd import Variable
import torch

import torchvision.transforms as transforms
import torchvision.models as models
import torchvision

#coding: utf-8
import webiopi
import os
import datetime
SAVEDIR = '/home/pi/ex6'
@webiopi.macro
def camera(no):
    filename = SAVEDIR + '/camera_' + no + '.jpg'
    command = 'fswebcam -r 320x240 -d /dev/video0 ' + filename #take a picture
    os.system(command)#写真を取る。
    os.system('sync')#未処理のデータをディスクに書き込む緊急用のコマンド
@webiopi.macro
def Time():
    now = datetime.datetime.now()
    now_datetime = (str(now.year) + " " + str(now.month) + " " +
    str(now.day) + " " + str(now.hour) + ":" + str(now.minute) + ":" +
    str(now.second))
    return now_datetime
    os.system('sync')

imsize=256
loader=transforms.Compose([transforms.Scale(imsize),transforms.ToTensor()])
@webiopi.macro
def image_Loader(image_name):
    image=Image.open(image_name).convert("RGB")
    image=loader(image)
    image=Variable(image,requires_grad=True)
    image=image.unsqueeze(0)
    return image
m=nn.Softmax(dim=1)

@webiopi.macro
def judge():
    """
    model.pthから学習したモデルで、写真を判定するプログラム
    """
    