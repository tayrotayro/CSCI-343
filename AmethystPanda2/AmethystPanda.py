# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:24:53 2018

Taylor Rotolo
AmethystPanda
October 1, 2018
Challenge 2

sources: 
Paul (TA)

Stack Overflow
https://stackoverflow.com/questions/2960772/how-do-i-put-a-variable-inside-a-string-in-python
https://stackoverflow.com/questions/9452108/how-to-use-string-replace-in-python-3-x
https://stackoverflow.com/questions/208120/how-to-read-and-write-multiple-files

W3schools (Python List)
https://www.w3schools.com/python/python_lists.asp

"""

import os as os
import numpy as np
import matplotlib.pyplot as mplot

lexi=[]
list=[]


lex=open("sentiment_lex.csv","r")
lex=lex.read()
lex=lex.split("\n")
del lex[-2]
del lex[-1]


for x in lex:
    x=x.split(",")
    x[1]=float(x[1])
    lexi.append(x)
    

    
sel = input("Please choose script a or b to analyze (type 'a' or 'b' below)\n")

if sel == 'a' or sel == 'b':
    Path = "C:/Users/Tayro/Documents/CSCI 343/AmethystPanda2/data_ch2/"
    filelist = os.listdir(Path)
    for i in filelist:
        if i.startswith(sel):  
            with open(Path + i, 'r') as f:
                for line in f:
                    line = line.replace(".", "")
                    line = line.replace(",", "")
                    line=line.replace("\n", "")
                    line = line.replace("]", " ")
                    line = line.replace("[", " ")
                    line = line.replace("!", "")
                    line = line.replace(":", "")
                    line = line.replace(";", "")
                    line = line.replace("?", "")
                    line = line.replace("'", "")
                    line = line.replace("(", " ")
                    line = line.replace(")", " ")
                    line = line.replace("-", " ")
                    list.append(line)
else:
    print("******Invalid input**********")
    

for z in list:
    z=z.split(" ")
    
    


"""Negative [-1.0, -0.6), Weakly Negative [-0.6, -0.2), Neutral [-0.2, 0.2], Weakly
Positive (0.2, 0.6], and Positive (0.6, 1.0]."""
    
neg=0
wneg=0
neu=0
wpos=0
pos=0
 

for x in lexi:
    for key in list:
        if (x[1] <= (-0.6) and x[1] >= (-1.0)):
            neg+=1
        if (x[1] <= (-0.2) and x[1] >= (-1.0)):
            wneg+=1
        if (x[1] <= (0.2) and x[1] >= (-0.2)):
            neu+=1
        if (x[1] <= (0.6) and x[1] >= (0.2)):
            wpos+=1
        if (x[1] <= (1.0) and x[1] >= (0.6)):
            pos+=1

xaxis=[]
xnames=["Neg", "W. Neg", "Neutral", "W.Pos", "Pos"]
yaxis=[]
xaxis.append(neg)
xaxis.append(wneg)
xaxis.append(neu)
xaxis.append(wpos)
xaxis.append(pos)
xaxis = np.log10(xaxis)


mplot.xticks(range(0,len(xnames)),xnames)
mplot.xlabel("Sentiment")
mplot.ylabel("Word Count log 10")
mplot.title("Sentiment Analysis for series " + sel)
mplot.bar(range(0,len(xaxis)), xaxis)
mplot.show()

    