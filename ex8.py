handle = open("ex8.txt",'r')
text = handle.readlines()

newlist=''

for i in text:
  newlist = newlist + i.rstrip('\n')

  
def maxp(x):
  l=len(x)
  p=1
  for i in range(l):
    p = p * int(x[i])
  return p

grand_max,a,b=1,0,0

for j in range(1000):
  if maxp(newlist[j:j+13]) > grand_max :
    grand_max,a = maxp(newlist[j:j+13]),j
  
print grand_max,a,newlist[a:a+13]