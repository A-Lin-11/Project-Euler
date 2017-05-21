def fac(x):
  if x == 1:
    return 1
  else:
    return fac(x-1) * x

d={0:1,1:1}
for i in xrange(2,10):
  d[i]=fac(i)

  
def cn(x):
  t=0
  for i in str(x):
    t+=d[int(i)]
  if t == x:
    return True
  else:
    return False
    
s = 0
for x in xrange(10,2540160):
  if cn(x):
    s += x
print s 