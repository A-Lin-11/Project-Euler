# -*- coding: utf-8 -*-
"""
Created on Wed May 31 10:43:00 2017

@author: andre
"""
from math import factorial

chain_length = 60

def chain(x):
    c = 0
    r = [x]
    while c < chain_length - 1:
        x = sum([factorial(int(i)) for i in str(x)])
        if x in r:
            return False
        r.append(x)
        c += 1
    
    x = sum([factorial(int(i)) for i in str(x)])
    return x in r   

res = 0
m = 1000000
for i in range(m):
    res += int(chain(i))
print(res)  
