def dec_len(x):
  l=[]
  n = 10**len(str(x))
  i,j= n/x , n%x
  while i not in l or i==0:
    l.append(i)
    i,j= j*n/x, j*n%x
    if j == 0:
      break
  return len(str(x)) * len(l)

m=n=0
for i in xrange(11,1000,2):
  if dec_len(i) > m:
    m,n = dec_len(i), i

print m,n