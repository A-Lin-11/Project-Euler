# -*- coding: utf-8 -*-
"""
Created on Wed May 31 21:54:58 2017

@author: andre
"""

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
        
x = 1
m = 1000000
p = gen_primes()
while x < m:
    q = next(p)
    x *= q
print(x/q)