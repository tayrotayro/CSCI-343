# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 15:00:37 2018

@author: Tayro

Taylor Rotolo
AmethystPanda
October 1, 2018
 Challenge 2

sources: 
Paul (TA)
Lecture material
"""
import numpy as np
import os
from PIL import Image
import matplotlib.pyplot as mplot


images=[]
data=[]


path = 'C:/Users/Tayro/Documents/CSCI 343/AmethystPanda3/AmethystPanda3/data_ch3a/AmethystPanda/einsteinatanderson/'
filelist=os.listdir(path)
for i in filelist:
    img = Image.open(path+i)
    img= np.float32(img)
    data.append(img)
    
#print(len(data))
    


avgimg=[0, 0, 0]


for i in range(0,len(data)):
    avgimg+=data[i]
    
avgimg = avgimg/len(data)

"""

stdimg=[0, 0, 0]
for i in data:
    stdimg=stdimg+(i-avgimg)**2

stdimg = np.sqrt(stdimg/len(data))
"""



user=input("Please enter the threshold value between 0-255: ")
user = float(user)


stdimg=np.std(data, 0)


if (0<=user<=255):
    for row in range(0, len(avgimg)):
        for col in range(0, len(avgimg[row])):
            if(stdimg[row][col] > [user, user, user]).any():
                avgimg[row][col]=[255,0,0]
            
    avgimg=np.clip(avgimg,0,255)
    stdimg=np.clip(stdimg,0,255)
    avgimg=np.uint8(avgimg)
    stdimg=np.uint8(stdimg)

    mplot.imshow(avgimg)
    mplot.show()

else: 
    print("************Invalid Input**************")



