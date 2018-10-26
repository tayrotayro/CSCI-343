# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 15:46:34 2018

@author: Tayro
"""

import numpy as np
import matplotlib.pyplot as mplot


data=open("AmethystPanda_ch1.csv","r")
data=data.read()
data=data.split("\n")

xaxis=[]
yaxis=[]
ampaverages=[]

for x in range(0,len(data)-1):
    data[x]=data[x].split(",")
    data[x][0]=np.float32(data[x][0])
    data[x][1]=np.float32(data[x][1])
    data[x][2]=np.float32(data[x][2])
    
    if data[x][2] > 16:
        
        xaxis.append(data[x][0])
        yaxis.append(data[x][1])
        
xset=list(set(xaxis))
xset.sort()
      
  
for y in range(0,len(xset)): 
    counter=0
    sum=0
    for x in range(0,len(xaxis)):
        if xaxis[x] == xset[y]:
           counter += 1
           sum += yaxis[x]
    final = sum/counter
    ampaverages.append(final)
         

print len(xset),len(ampaverages)
        

        
mplot.scatter(xaxis, yaxis)
mplot.plot(xset, ampaverages)
mplot.xlabel("Transmission Time (miliseconds)")
mplot.ylabel("Signal Amplitude")
mplot.title("Weather Transmission Radio Frequency")
mplot.show()
    
    

