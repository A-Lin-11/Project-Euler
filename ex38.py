def pm(x,y):
  l=[]
  for i in xrange(1,y+1):
    z = str(x*i)
    for j in z:
      l.append(int(j))
      sl=set(l)
      q = sorted(l)
  if q == [1,2,3,4,5,6,7,8,9]:
    return l


def f(x):
  l=[]
  for i in str(x):
    if i in l:
      return False
    else:
      l.append(i)
  return True
  
an=[]
for i in xrange(10,10000):
  if f(i):
    if i < 100:
      for j in [4,5]:
        if pm(i,j)!=None:
          an.append(pm(i,j))
          print i
    elif i < 1000:
      if pm(i,3)!=None:
        an.append(pm(i,3))
        print i
    else:
      if pm(i,2)!=None:
        an.append(pm(i,2))
        print i
print max(an)