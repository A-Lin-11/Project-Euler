# -*- coding: utf-8 -*-
"""
Created on Wed May 31 18:34:25 2017

@author: andre
"""
import functools

with open('p079_keylog.txt') as f:
    df = []
    for i in f.readlines():
        df.append(i[:-1])
        
number_list = list(set(functools.reduce(lambda x,y: x+y, df)))

number_net = {str(k):[] for k in number_list}
for i in df:
    number_net[i[0]].append(i[1])
    number_net[i[0]].append(i[2])
    number_net[i[1]].append(i[2])

for i in number_net:
    number_net[i] = list(set(number_net[i]))
    
code_initial = ''.join(sorted(number_list, reverse=True, key = lambda x: len(number_net[x])))

print(code_initial)
