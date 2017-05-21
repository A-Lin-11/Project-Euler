def is_prime(x):
  for i in xrange(2, int(x**0.5)+1):
    if x % i == 0 :
      return False
  return True

primes = [] 
for i in xrange(1000,10000):
  if is_prime(i):
    primes.append(i)

def pm(x,y):
  lx,ly=[],[]
  for i in str(x):
    lx.append(i)
  for j in str(y):
    ly.append(j)
  lx.sort()
  ly.sort()
  if lx == ly:
    return True
  return False

for i in xrange(len(primes)-4):
  for j in xrange(i+1,len(primes)-3):
    a, b = primes[i], primes[j]
    if pm(a,b):
      c = b * 2 - a
      if pm(a,c):
        if c in primes:
          print a,b,c