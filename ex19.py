from datetime import date

start_date = date(1900,1,7)

t=0

for y in xrange(1901,2001):
  for m in xrange(1,13):
    if (date(y,m,1) - start_date).days%7==0:
      t+=1 

print t