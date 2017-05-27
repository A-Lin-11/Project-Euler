# -*- coding: utf-8 -*-
"""
Created on Sat May 27 01:22:26 2017

@author: andre
"""
from math import log, ceil, pow

'''
10^(n-1) <= k^n < 10^n
10^(1-1/n) <= k < 10

'''
def pc(n):
    if n == 1:
        return 9
    min, max = ceil(pow(10,(1-1/n))), 10
    return max - min
a = pc(2)

print(sum([pc(n) for n in range(1,100)]))
