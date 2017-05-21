def fac(x):
  lst = []
  for i in xrange(2,int(x**0.5)+1):
    if x % i == 0:
      lst.append(i)
  return len(lst)*2+2
  
t = [1,3]
i=3
while fac(t[-1])<=500:
  t.append(t[-1]+i)
  i = i + 1
else:
  print t[-1]