# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 12:34:54 2017

@author: andre
"""


def gpn(n):
    r = []
    i = 1
    k = int((3*i*i-i)/2)
    while k <=n:
        r.append((k,(-1)**(abs(i)-1)))
        if i>0:
            i = -i
        else:
            i = -i+1
        k = int((3*i*i-i)/2)
    return r

print(gpn(100))
        

d = {0:1,
     1:1,
     2:2,
     3:3,
    }

def f(s):
    if s < 0:
        return 0

    if s in d:
        return d[s]
    k = sum([i[1]*f(s-i[0]) for i in gpn(s)])
    d[s] = k
    return k

print(f(100)-1)
