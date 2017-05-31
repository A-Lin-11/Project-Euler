# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from fractions import Fraction

m = 10**6
res = 0
for i in range(4,m+1):
    numerator = int(i*3/7)
    x = Fraction(numerator,i)
    if x > res and x < Fraction(3,7):
        res = x

print(res)
