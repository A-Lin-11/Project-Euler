def lp(x,y):
  g = dict()
  for i in xrange(x+1):
    g[i]=i+1
  for j in xrange(y-1):
    for i in xrange(1,x+1):
      g[i] = g[i]+g[i-1]
  return int(g[x])
  
print lp(20,20)