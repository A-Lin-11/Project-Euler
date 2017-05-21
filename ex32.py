def dig_used(x):
  l=[]
  for i in str(x):
    l.append(i)
  if len(l)== len(set(l)):
    return True
  else:
    return False

c=[]
for x in xrange(2,99):
  if dig_used(x):
    for y in xrange(x,5000):
      if dig_used(y):
        if dig_used(x*y):
          s=str(x)+str(y)+str(x*y)
          if dig_used(int(s)):
            if len(s) == 9 and '0' not in s:
              c.append(x*y)
print sum(set(c))