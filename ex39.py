ps=[]
for n in xrange(2,int(500)+1):
  ps.append(n**2)

s={}

for i in xrange(len(ps)):
  for j in xrange(i,len(ps)):
    t= ps[i] + ps[j]
    if t in ps:
      q = ps[i]**0.5 + ps[j]**0.5 + t**0.5
      if q <=1000:
        if s.get(q):
          s[q] += 1
        else:
          s[q] =1
ss ={}
for i in s:
  ss[s[i]]=i
print ss[max(ss)]