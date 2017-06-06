# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 12:11:35 2017

@author: andre
"""



def f(max_number):
    q = int((max_number/2)**0.5)
    d = {}
    for m in range(2,q):
        for n in range(1,m):
            a,b,c = min(m**2-n**2, 2*m*n),max(m**2-n**2, 2*m*n), m**2+n**2
            k = a+b+c
            x,y,z = a,b,c
            while k < max_number:
                d[(x,y,z)] = True
                x += a
                y += b
                z += c
                k = x+y+z
    return d

res = {}

for (a,b,c) in f(1500000):
    k = a+b+c
    res[k] = res.get(k,0) + 1
    
r = 0
for i in res:
    if res[i] == 1:
        r += 1
        
print(r)
