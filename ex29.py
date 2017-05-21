l=[]

lim = 100

for a in xrange(2,lim+1):
  for b in xrange(2,lim+1):
    l.append(a**b)
    
print len(set(l))