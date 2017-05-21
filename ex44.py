def pn(x):
  if ((24*x+1)**0.5+1)/6%1==0:
    return True
  return False
  
def p(x):
  return x*(3*x-1)*0.5

def pp(a,b):
  if pn(a-b) and pn(a+b):
    return True
  return False
  
l=[]
for i in xrange(1,4000):
  l.append(int(p(i)))
  
d=100000000000
for i in xrange(len(l)-1):
  for j in xrange(i+1,len(l)):
    if pn(l[j]+l[i]):
      if pn(l[j]-l[i]):
        d=min(l[j]-l[i],d)

print d     

