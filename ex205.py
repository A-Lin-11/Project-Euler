# -*- coding: utf-8 -*-
"""
Created on Wed May 31 23:59:30 2017

@author: andre
"""

from itertools import product

peter = {}
colin = {}

a = [sum(i) for i in product(range(1,5), repeat=9)]

for i in a:
    peter[i] = peter.get(i,0) + 1
    
for i in peter:
    peter[i] = peter[i] / len(a)
    
b = [sum(i) for i in product(range(1,7), repeat=6)]

for i in b:
    colin[i] = colin.get(i,0) + 1
    
for i in colin:
    colin[i] = colin[i] / len(b)
    
    
r = 0
for i in peter:
    for j in range(6,i):
        r += peter[i] * colin[j] 
        
print(r)
