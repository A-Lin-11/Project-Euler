# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 16:40:56 2017

@author: andre
"""

def b(x):
    if str(x) == ''.join(sorted(str(x))) or str(x) == ''.join(sorted(str(x))[::-1]):
        return False
    return True


d = {}
r = 0
c = 100
while r < 0.99:
    
    if b(c):
        d[c] = True
    r = len(d)/c
    c += 1
    
print(c-1)
