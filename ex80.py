# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 01:11:13 2017

@author: andre
"""

from mpmath import mp

def f(x):
    s = 0
    mp.dps = 110
    r = (mp.sqrt(x))
    r = str(r)
    for i in r[:101]:
        if i != '.':
            s += int(i)
    return s
    

res = 0

for i in range(101):
    if i**0.5 != int(i**0.5):
        res += f(i)
        
print(res)
