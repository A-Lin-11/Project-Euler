def is_prime(x):
  for i in xrange(2, int(x**0.5)+1):
    if x % i == 0 :
      return False
  return True

prime=[]  
for i in xrange (3,int(1000)):
  if is_prime(i):
    prime.append(i)  
  
maxp = aa=bb = 0

for a in xrange(-997,1000,2):
  if a > 0:
    for b in prime:
      n = 1
      while is_prime(n*n+n*a+b):
        n = n+1
      if n>maxp:
        maxp , pd = n , a*b
  else:
    for b in [x for x in prime if -a+2<=x and x<1000]:
      n = 1
      while is_prime(n*n+n*a+b):
        n = n+1
        if n*n+n*a+b < 0:
          break
      if n>maxp:
        maxp , aa,bb = n , a,b      
      
print maxp , aa, bb , aa*bb