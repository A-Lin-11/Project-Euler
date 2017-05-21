def layer(x):
  s=1
  for i in xrange(3,x+1,2):
    s += i**2*4 -6*(i-1)
  return s
  
print layer(1001)