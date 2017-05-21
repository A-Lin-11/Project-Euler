def ds(x,p):
  s = 0
  for i in str(x):
    s += int(i)**p
  return s
  
s=0
for i in xrange(10,600000):
  if ds(i,5) == i:
    s += i

print s 