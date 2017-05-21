n=d=1
for i in xrange(100,1000):
  if i%111!=0 and i%100!=0:
    t=str(i)
    if int(t[0])*int(t[1:]) == int(t[:2])*int(t[2]):
      n *= min(int(t[0]),int(t[2]))
      d *= max(int(t[0]),int(t[2])) 
      print min(int(t[0]),int(t[2])), max(int(t[0]),int(t[2]))
print n,d