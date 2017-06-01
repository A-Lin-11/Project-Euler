# -*- coding: utf-8 -*-
"""
Created on Wed May 31 22:48:22 2017

@author: andre
"""
import re
import timeit

start = timeit.default_timer()

print((1020304050607080900)**0.5,(19293949596979899900)**0.5)

for i in range(1010101010,4392487859,10):
    x = str(i**2)
    if re.search('^1\d2\d3\d4\d5\d6\d7\d8\d9\d0$',x):
        print(i,x)
        break
         

stop = timeit.default_timer()

print(stop - start, 'seconds')
