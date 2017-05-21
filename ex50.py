def is_prime(x):
  for i in xrange(2, int(x**0.5)+1):
    if x % i == 0 :
      return False
  return True

primes = [] 
for i in xrange(2,8000):
  if is_prime(i):
    primes.append(i)

l={}
for i in xrange(len(primes)-3):
  for j in xrange(i+1,len(primes)-2):
    s = sum(primes[i:j])
    if s<1000000:
      if is_prime(s):
        if s not in l or l[s]<j-i:
          l[s]=j-i

import operator
max_sum = max(l.iteritems(), key=operator.itemgetter(1))[0]
print max_sum, l[max_sum]