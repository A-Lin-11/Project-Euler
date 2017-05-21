def ds(x):
  s=0
  for i in str(x):
    s+=int(i)
  return s
  
def fac(x):
  y=2
  for i in xrange(3,x+1):
    y*=i
  return y
  
print ds(fac(100))