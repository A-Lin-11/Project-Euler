count = 2

def is_prime(x):
  for i in xrange(2, int(x**0.5)+1):
    if x % i == 0 :
      return False
  return True

p=3  
while count < 10001:
  p=p+2
  if is_prime(p):
    count=count+1

print p