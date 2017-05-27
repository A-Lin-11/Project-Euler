# -*- coding: utf-8 -*-
"""
Created on Fri May 26 18:36:53 2017

@author: andre
"""
def concat(a,b):
    return int(str(a)+str(b))

def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0 :
            return False
    return True

m = 11000   # max number for prime number generator

prime_dict = { v:is_prime(v) for v in range(3,m)}
prime_list = [i for i in prime_dict if prime_dict[i]]

f2, f3, f4, f5 = [], [], [], []

f2_dict = {}  # stores all the posible pairs in a dict.

for i in range(len(prime_list)-1):
    for j in range(i+1,len(prime_list)):
        x,y = prime_list[i], prime_list[j]
        if is_prime(concat(x,y)) and is_prime(concat(y,x)):
            f2.append([x,y])
            if x in f2_dict:
                f2_dict[x].append(y)
            else:
                f2_dict[x] = [y]

for i in f2:
    for j in f2_dict[i[0]]:
        if (i[1] in f2_dict) and (j in f2_dict[i[1]]):
            f3.append([i[0], i[1], j])
     


for i in f3:
    for j in f2_dict[i[0]]:
        if (i[1] in f2_dict) and (j in f2_dict[i[1]]):
            if (i[2] in f2_dict) and (j in f2_dict[i[2]]):
                f4.append([i[0], i[1], i[2], j])


f4_primes = []
for i in f4:
    for j in i:
        if j not in f4_primes:
            f4_primes.append(j)

       
for i in f4:
    for j in f4_primes:
        if (i[0] in f2_dict) and (j in f2_dict[i[0]]):
            if (i[1] in f2_dict) and (j in f2_dict[i[1]]):
                if (i[2] in f2_dict) and (j in f2_dict[i[2]]):
                    if (i[3] in f2_dict) and (j in f2_dict[i[3]]):
                        f5.append([i[0], i[1], i[2], i[3], j])
                        
print([(i, sum(i)) for i in f5])
