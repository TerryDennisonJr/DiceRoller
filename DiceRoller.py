#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 20:08:40 2021

@author: terrydennison
"""
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np

def func(num):
   
    diceNum= ['One', 'Two', 'Three', 'Four', 'Five', 'Six'] 
   
    roller = np.random.randint(1,7,1)
    
    for i in roller:
        if i not in dic:
            dic[i] =1
        else:
            dic[i]+=1 
    rollFreq = [dic[i] for i in sorted(dic.keys())]
    
    plt.clf()
   
    for i in range(len(rollFreq)):
        plt.text(i,rollFreq[i],f'{(rollFreq[i]/num_of_updates)*100:.1f}%\n', color = 'k', ha = 'center')
    for i in range(len(rollFreq)):
        plt.text(i,rollFreq[i],f'{rollFreq[i]}\n\n', color = 'k', ha = 'center')
    plt.xlabel("Dice Number")
    plt.ylabel('Frequencies')
    
    plt.bar(diceNum,rollFreq,color= ['r','g','k','y','c','b'])
    plt.ylim(1,200)
  
dic = {}
rollFreq  =[]
diceNum=[]

num_of_updates = 999
run = animation.FuncAnimation(plt.figure("Rolling a Six-Side Die "f'{num_of_updates+1}'" times"),func, repeat = False, frames = num_of_updates, interval =30)   



