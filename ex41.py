def is_prime(x):
  for i in xrange(2, int(x**0.5)+1):
    if x % i == 0 :
      return False
  return True
  
from itertools import permutations

t=[]
m = 9
while t == []:
  m = m-1
  l=[]
  for i in xrange(1,m):
    l.append(str(i))

  s=[]
  for i in permutations(l,m-1):
    j = int(''.join(i))
    if j%2==1:
      if j%5!=0:
        s.append(int(''.join(i)))
        
  t = []
  for i in s:
    if is_prime(i):
      t.append(i)
      
print max(t)