def df(n):
  s = ''
  q=1
  while len(s)<n:
    s += str(q)
    q += 1
  return s[n-1]
  
print df(12)

t = 1
for i in xrange(7):
  t *= int(df(10**i))
  
print  t
  