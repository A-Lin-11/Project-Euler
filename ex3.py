prime = []

def is_prime(x):
  for i in xrange(2, int(x**0.5)+1):
    if x % i == 0 :
      return False
  return True

n = 600851475143  

for i in xrange (2,int(n**0.5)):
  if is_prime(i):
    prime.append(i)


largest_prime = 2
for q in prime:
  while n % q == 0:
    n = n/q
    largest_prime = q

print largest_prime
