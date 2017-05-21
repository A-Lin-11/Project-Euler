def is_prime(x):
  for i in xrange(2, int(x**0.5)+1):
    if x % i == 0 :
      return False
  return True

primes = [] 
for i in xrange(2,150500):
  if is_prime(i):
    primes.append(i)

  
def dpf(x):
  l=[]
  k = 0
  f = 0
  while f<=x:
    f = primes[k]
    while x%f==0:
      if f not in l:
        l.append(f)
      x = x / f
    k = k + 1
    
  return l

i = 10
c = True
while c:
  i += 1
  if len(dpf(i))==4:
    if len(dpf(i+1))==4:
      if len(dpf(i+2))==4:
        if len(dpf(i+3))==4:
          c = False
print i