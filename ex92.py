# -*- coding: utf-8 -*-
"""
Created on Sat May 27 02:14:48 2017

@author: andre
"""

def chain(x):
    s = 0
    for i in str(x):
        s += int(i)**2
    return s

get_89_dict = {}

def get_89(c):
    x = c
    while x!= 1 and x!=89:

        if x in get_89_dict:
            return get_89_dict[x]
        
        x = chain(x)

    if x == 89:
        get_89_dict[c] = True
        return True
    get_89_dict[c] = False
    return False

res = 0
for i in range(1,10000000):
    if get_89(i):
        res += 1
        
print(res)
