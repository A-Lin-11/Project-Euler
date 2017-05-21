def b2(x):
  i, j = x/2, x%2
  l=[]
  while i>0:
    l.append(j)
    i,j=i/2,i%2
  l.append(1)
  return l[::-1]
  
lim = 1000000
an= 0
for i in xrange(lim):
  if str(i) == str(i)[::-1]:
    if b2(i) == b2(i)[::-1]:
      an += i
print an