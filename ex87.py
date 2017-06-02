# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 00:54:23 2017

@author: andre
"""
m = 50000000

def gen_primes():

    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]        
        q += 1
        
p2 = {}
p3 = {}
p4 = {}
r = {}

for i in gen_primes():
    if i**2 > m:
        break
    p2[i**2]=True
    p3[i**3]=True
    p4[i**4]=True
    
for i in list(p3):
    if i > m:
        p3.pop(i, None)
        
for i in list(p4):
    if i > m:
        p4.pop(i, None)
       
for i in p2:
    for j in p3:
        for k in p4:
            if i+j+k<m:
                r[i+j+k]=True
                
print(len(r))
