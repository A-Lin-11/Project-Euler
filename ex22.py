def sc(x):
  s=0
  for i in x:
    s = s + ord(i)-64
  return s

handle = open("ex22.txt","r")
names = handle.read()
names = names.split(",")
names.sort()

t=0
for i in xrange(len(names)):
  t=t + sc(names[i].replace('\"','')) * (i+1)
  
print t