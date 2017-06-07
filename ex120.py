# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 17:28:16 2017

@author: andre
"""

#def f(x,n):
#    k = (x-1)**n + (x+1)**n
#    return k%(x**2)
#
#for i in range(1,120,2):
#    print(f(51,i))

r = 0
for i in range(3,1001):
    if i%2==0:
        r += i*(i-2)
    else:
        r += i*(i-1)
print(r)
