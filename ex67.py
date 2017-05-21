h = open("ex67.txt",'r')
t = h.readlines()

l=[]
for i in t:
  q = i.split()
  l.append(q)

l = l[::-1]
for i in l:
  for j in xrange(len(i)):
    i[j] = int(i[j])

nl=l    
for x in xrange(1,len(nl)):
  for n in xrange(len(nl[x])):
    nl[x][n]=nl[x][n]+max(nl[x-1][n],nl[x-1][n+1])
print nl[-1]