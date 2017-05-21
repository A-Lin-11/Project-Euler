prime = []

def is_prime(x):
  for i in xrange(2, int(x**0.5)+1):
    if x % i == 0 :
      return False
  return True

n = 1000000  

for i in xrange (3,int(n)):
  if is_prime(i):
    prime.append(i)

    
def test_p(x):
  for i in str(x):
    if i not in ['1','3','7','9']:
      return False
  for j in xrange(len(str(x))):
    p = str(x)[j+1:] + str(x)[:j+1]
    if not is_prime(int(p)):
      return False
  return True
  
s = 2                                   # 2 and 5
for i in prime:
  if test_p(i):
    s += 1
print s