def pt(a,b,c):
  if a*a+b*b-c*c==0:
    return True
  else:
    return False


i=1
j=1

while not pt(i,j,1000-i-j):
  j=j+1
  if j*2 >= 1000-i:
    i=i+1
    j=500-i
    

print "a=%d, b=%d, c=%d, a^2=%d, b^2=%d, c^2=%d, product of abc is %d)" % (
i,j,1000-i-j, i*i,j*j, (1000-i-j)**2, i*j*(1000-i-j))

