k=0

for i in xrange(1,1001):
  k += int(str(i**i)[-10:])
print str(k)[-10:]