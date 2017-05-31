# -*- coding: utf-8 -*-
"""
Created on Wed May 31 12:04:43 2017

@author: andre
"""

from fractions import Fraction
from math import gcd

m = 12000
res = 0
for i in range(4,m+1):
    numerator_low = int(i/3)+1
    numerator_high = int(i/2 + 0.5)
    for j in range(numerator_low, numerator_high):
        if gcd(i,j) == 1:    
            res += 1

print(res)
