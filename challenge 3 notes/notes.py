# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:23:48 2018

@author: Tayro
"""

import numpy as np
import matplotlib.pyplot as mplot

import image

img = Image.open("mgb.jpg")
img=np.float64(img)


img1=image.open("jag.jpg")
img1=np.gloat64(img1)

avg_img=img+img1

avg_img=avg_img/2.0

for row in range(0, len(avg_img)):
    for col in range(0, len(avg_img[row])):
        if(avg_img[row][col] < [100, 100, 100]).any()
            

avg_img=np.clip(avg_img, 0, 255)
avg_img=np.uint8(avg_img)

mplot.imshow(avg_img)
mplot.show()