# -*- coding: utf-8 -*-
"""
Created on Sat May 27 02:02:28 2017

@author: andre
"""

def permute(x):
    return ''.join(sorted(str(x)))

cubic_dict =  {}

base_number = 345
found = False
num_of_permutations = 5

while not found:
    k = permute(base_number**3)
    if k not in cubic_dict:
        cubic_dict[k] = [base_number**3]
    else:
        cubic_dict[k].append(base_number**3)
        if len(cubic_dict[k]) >= num_of_permutations:
            print(min(cubic_dict[k]))
            found = True
    base_number += 1
