def col(x):
  c=0
  while x!=16:
    if x%2==0: 
      x = x/2
    else:
      x = x*3+1
    c = c + 1
  return c
  
m=0
n=0
for x in xrange(500000,1000000):
  if col(x)>m:
    m = col(x)
    n = x

print m,n