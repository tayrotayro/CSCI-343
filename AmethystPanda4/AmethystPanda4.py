"""
Spirit Animal: Amethyst Panda
Date: 10/30/18
Challenge:4 


Sources:
    Paul
    stack overflow
    w3shcools
"""
import numpy as np
import matplotlib.pyplot as mplot
import math


data1=open("us_outline.csv","r")
data1=data1.read()
data1=data1.split("\n")

data2=open("data.csv","r")
data2=data2.read()
data2=data2.split("\n")

means=[]
usx=[]
usy=[]
xaxis=[]
yaxis=[]
color=[]

"""have a list of each grid point of both x and y x=[] and y=[] and the average color c=[]
then calculate the distance and keep track of each """

for x in range(0,len(data1)):
    data1[x]=data1[x].split(",")
    usx.append(np.float64(data1[x][0]))
    usy.append(np.float64(data1[x][1]))

for x in range(0,len(data2)):
    data2[x]=data2[x].split(",")
    xaxis.append(np.float64(data2[x][0]))
    yaxis.append(np.float64(data2[x][1]))
    color.append(np.float64(data2[x][2]))


kval=input("Please enter a k-value greater than 0: ")
kval = int(kval)

value=0
xvals=[]
yvals=[]

if kval>0: 
    for i in range(0,194):
        for j in range(0,120):
            distance=[]
            value=0
            xvals.append(i)
            yvals.append(j)
            for k in range(0,len(xaxis)):
                dis = math.sqrt(math.pow(i-xaxis[k],2)+math.pow(j-yaxis[k],2))
                distance.append([dis,color[k]])
            distance.sort(key=lambda x:x[0])
            for l in range(0,kval):
                value+=distance[l][1]
            mean=value/kval
            means.append(mean)
            

                     
    mplot.plot(usx,usy)               
    mplot.scatter(xvals, yvals, c=means, cmap='viridis')
        
else:
    print("********Invalid Input*********")
    

    
 