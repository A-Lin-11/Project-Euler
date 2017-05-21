def pal(x):
  if str(x)==str(x)[::-1]:
    return True
  else:
    return False

p,a,b=0,0,0
for i in range(100,1000):
  for j in range(i,1000):
    if pal(i*j):
      if i*j > p:
        p,a,b=i*j,i,j
      

print p,a,b