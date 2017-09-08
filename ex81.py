# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 16:12:02 2017

@author: andre
"""

f = open('p081_matrix.txt')
f = f.readlines()

df = []
for i in f:
    df.append([int(q) for q in i.split(',')])

a = []

n = len(df)

for m in range(n*2-1):
    r = []
    for i in range(m+1):
        if m <= n-1:
            r.append(df[i][m-i])

    
        else:
            if i<n and m-i<n:
                r.append(df[i][m-i])

        
    a.append(r)
        
res = a[::-1]
res2 = [res[0]]

for i in range(1,n*2-1):

    if i < n:
        
        q = [res[i][0]+res2[i-1][0]]
        for j in range(1,i):
            x = res[i][j]+min(res2[i-1][j-1],res2[i-1][j])
            q.append(x)
        q.append(res[i][-1]+res2[i-1][-1])
    else:
        q = []
        for j in range(len(res[i])):
            x = res[i][j]+min(res2[i-1][j],res2[i-1][j+1])
            q.append(x)
          
    res2.append(q)
    
print(res2[-1])
