def is_prime(x):
  for i in xrange(2, int(x**0.5)+1):
    if x % i == 0 :
      return False
  return True
  
x = 33
c = True
while c:
  x += 2
  while is_prime(x):
    x += 2
  c = False
  for i in xrange(1,int((x/2)**0.5)+1):
    if is_prime(x - 2 * i * i):
      c = True
  if x > 10000:
    print "too small"
    break

print x