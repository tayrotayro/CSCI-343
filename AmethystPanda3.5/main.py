# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:53:41 2018

@author: Tayro
"""
import urllib.request
import time
import random
import numpy as np


guess="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
guess=list(guess)

usedguess=[]
password="12345678"
password=list(password)
start=time.time()

i=1

original=0

for x in password:
    randomguess=random.choice(guess)

    

    if randomguess in usedguess:
        randomguess=random.choice(guess)
    else:
        for x in password:
            password=int(password[x])
            password.insert(password.index(i), randomguess)
print(password)
        

        
"""
        randomguess.append(usedguess)
        password.join(password)
        with urllib.request.urlopen('https://john.cs.olemiss.edu/~jones/csci343/pwd/index.php?username=AmethystPanda&password='+password) as response:
            result = response.read()

        try:
            result=result.split()
            result=np.float64(result[0])
            if result>original:
                x = x+1
                original = result
            elif result<=original:
                original=result
        except:
            elif result=="SUCCESSFUL":
                print(password)
"""
        
            
   
   



        
        
        
        


        
        
        
        
