def factors(x):    
    return list(set(reduce(list.__add__, 
        ([i, x//i] for i in range(1, int(x**0.5) + 1) if x % i == 0))))

def sf(x):
  return sum(factors(x))-x

l=[]
for m in xrange(4,10001):
  n=sf(m)
  if sf(n)==m and m!=n:
    l.append(m)
    l.append(n)

print sum(set(l))