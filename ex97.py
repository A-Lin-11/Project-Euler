# -*- coding: utf-8 -*-
"""
Created on Wed May 31 16:07:11 2017

@author: andre
"""

def last_ten_digit_power(x,y):
    k = 1
    while y > 0:
        
        k *= x
        k = int(str(k)[-10:])
        y -= 1
    return k

print(str(last_ten_digit_power(2,7830457)*28433+1)[-10:])
