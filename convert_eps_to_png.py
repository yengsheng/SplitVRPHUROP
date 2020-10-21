# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 19:35:30 2020

@author: Yong Sheng
"""

from PIL import Image

image_eps = "C:\\Users\\Yong Sheng\\Desktop\\UROP\\SplitVRPHUROP\\SDVRP instances\\p11\\p11_1030_tsplib0_splitx10_0.eps"
im = Image.open(image_eps)
fig = im.convert('RGBA')
image_png = 'logo-rgb.png'
fig.save(image_png, lossless = True)
