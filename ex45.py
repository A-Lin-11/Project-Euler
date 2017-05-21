t=[]
for i in xrange(1,100000):
  t.append(int(i*(i+1)/2))
  
def p(x):
  if ((24*x+1)**0.5+1)/6%1==0:
    return True
  return False
  
def h(x):
  if ((8*x+1)**0.5+1)/4%1==0:
    return True
  return False
  
c=0
k=0
while c<2:
  k+=1
  if p(t[k]):
    if h(t[k]):
      print t[k]
      c+=1