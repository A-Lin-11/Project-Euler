prime = []

def is_prime(x):
  for i in xrange(2, int(x**0.5)+1):
    if x % i == 0 :
      return False
  return True


l3=[]
for a1 in [1,3,7,9]:
  for a2 in [1,3,7,9]:
    for a3 in [1,3,7,9]:
      control = True
      st=str(a1)+str(a2)+str(a3)
      for i in xrange(3):
        p = st[i+1:] + st[:i+1]
        if not is_prime(int(p)):
          control = False
      if control:
        for i in xrange(3):
          l3.append(int(st[i+1:] + st[:i+1]))


          
l4=[]
for a1 in [1,3,7,9]:
  for a2 in [1,3,7,9]:
    for a3 in [1,3,7,9]:
      for a4 in [1,3,7,9]:
        control = True
        st=str(a1)+str(a2)+str(a3)+str(a4)
        for i in xrange(4):
          p = st[i+1:] + st[:i+1]
          if not is_prime(int(p)):
            control = False
        if control:
          for i in xrange(4):
            l4.append(int(st[i+1:] + st[:i+1]))

           
l5=[]
for a1 in [1,3,7,9]:
  for a2 in [1,3,7,9]:
    for a3 in [1,3,7,9]:
      for a4 in [1,3,7,9]:
        for a5 in [1,3,7,9]:
          control = True
          st=str(a1)+str(a2)+str(a3)+str(a4)+str(a5)
          for i in xrange(5):
            p = st[i+1:] + st[:i+1]
            if not is_prime(int(p)):
              control = False
          if control:
            for i in xrange(5):
              l5.append(int(st[i+1:] + st[:i+1]))           

l6=[]
for a1 in [1,3,7,9]:
  for a2 in [1,3,7,9]:
    for a3 in [1,3,7,9]:
      for a4 in [1,3,7,9]:
        for a5 in [1,3,7,9]:
          for a6 in [1,3,7,9]:
            control = True
            st=str(a1)+str(a2)+str(a3)+str(a4)+str(a5)+str(a6)
            for i in xrange(6):
              p = st[i+1:] + st[:i+1]
              if not is_prime(int(p)):
                control = False
            if control:
              for i in xrange(6):
                l6.append(int(st[i+1:] + st[:i+1]))

print 13 + len(set(l3)) + len(set(l4)) + len(set(l5)) + len(set(l6))
print set(l3+l4+l5+l6)