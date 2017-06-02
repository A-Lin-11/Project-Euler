# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 16:09:01 2017

@author: andre
"""
from itertools import product


r = 0

# Count the ones where the right angle is in on the axis
for i in range(1,51):
    for j in range(1,51):
        r += 3


# Count the ones where the right angle is in the middle
        
x = list(product(range(51), range(51)))

res = {}
for i in x:
    for j in x:
        x1,y1 = i
        x2,y2 = j
        if x1!=x2 and y1!=y2 and x1+y1>0:
            if x1*x2+y1*y2==x1*x1+y1*y1:
                k = ((x1,y1),(x2,y2))
                res[k] = True


print(r + len(res))
