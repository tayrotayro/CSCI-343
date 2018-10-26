# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 15:00:37 2018

@author: Tayro
"""
from os import listdir
from os.path import isfile, join
import numpy
import cv2

mypath='C:\Users\Tayro\Downloads\data_ch3a.zip\AmethystPanda\einsteinatanderson'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  images[n] = cv2.imread( join(mypath,onlyfiles[n]) )
  
print(images)