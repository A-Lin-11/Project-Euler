# -*- coding: utf-8 -*-
"""
Created on Wed May 31 18:22:59 2017

@author: andre
"""
from math import log

with open('p099_base_exp.txt') as f:
    df = []
    for i in f.readlines():
        m,n = i.split(',')
        df.append([int(m),int(n)])
        
q = 0
r = 0
for n,(x,y) in enumerate(df):
    if y*log(x) > q:
        q = y*log(x)
        r = n

print(r+1)
