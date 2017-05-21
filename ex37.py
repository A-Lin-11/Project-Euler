def is_prime(x):
  if x==1:
    return False
  else: 
    for i in xrange(2, int(x**0.5)+1):
      if x % i == 0 :
        return False
  return True

l=[]

def tp(x):
  if is_prime(x):
    for i in xrange(len(str(x))-1):
      a = int(str(x)[:i+1])
      b = int(str(x)[i+1:])
      if not is_prime(a) or not is_prime(b):
        return False
    return True
  return False

q=11  
while len(l)<11:
  if tp(q):
    l.append(q)
  q += 2

print l,sum(l)
