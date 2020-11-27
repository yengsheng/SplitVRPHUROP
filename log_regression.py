# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:41:53 2020

@author: Yong Sheng
"""

import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.datasets as dsets
import matplotlib.pyplot as plt
import numpy as np

train_dataset = dsets.MNIST(root = './data', train=True, transform=transforms.ToTensor(), download=True)

train_dataset[0][0].numpy().shape
show_img = train_dataset[0][0].numpy().reshape(28, 28)
plt.imshow(show_img, cmap='gray')
