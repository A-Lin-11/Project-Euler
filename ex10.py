prime = []

def is_prime(x):
  for i in xrange(2, int(x**0.5)+1):
    if x % i == 0 :
      return False
  return True

n = 2000000

for i in xrange (2,n):
  if is_prime(i):
    prime.append(i)
    
print sum(prime)