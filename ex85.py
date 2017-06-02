# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 00:40:58 2017

@author: andre
"""

def rec_count(x,y):
    r = 0
    for i in range(1,x+1):
        for j in range(1,y+1):
            r += i*j
            
    return r

d = 2000000
for i in range(1,200):
    for j in range(i,201):
        q = rec_count(i,j)
        if abs(q-2000000)<d:
            d = abs(q-2000000)
            r = (i,j,i*j)
            
print(d,r)
