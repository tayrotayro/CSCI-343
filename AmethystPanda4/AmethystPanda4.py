import numpy as np
import matplotlib.pyplot as mplot

data=open("us_outline.csv","r")
data=data.read()
data=data.split("\n")

xaxis=[]
yaxis=[]
ampaverages=[]

for x in range(0,len(data)):
    data[x]=data[x].split(",")
    xaxis.append(np.float32(data[x][0]))
    yaxis.append(np.float32(data[x][1]))
    
mplot.plot(xaxis, yaxis)
mplot.show()
  
print (xaxis)
print (yaxis)
    
 