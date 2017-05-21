def factors(x):    
    return list(set(reduce(list.__add__, 
        ([i, x//i] for i in range(1, int(x**0.5) + 1) if x % i == 0))))
        
def sf(x):
  return sum(factors(x))-x

limit = 28125
an=list(x for x in range(1,limit+1) if sf(x)>x)

l=range(limit+1)
for i in an:
  if i> limit/2:
    break
  for j in an[an.index(i):]:
    if i+j>limit:
      break
    l[i+j]=0

print sum(l)