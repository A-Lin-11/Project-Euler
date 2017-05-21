t = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}
tt = {10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8}
sd = {2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}

def wl(x):
  if x<10:
    return t[x]
  elif x<100:
    if x>=20:
      return sd[x/10]+t[x%10]
    else:
      return tt[x]
  elif x<1000:
    if x%100 !=0:
      return 10 + t[x/100] + wl(x%100)
    else:
      return 7 + t[x/100]
  else:
    return 3+8

s=0    
for i in xrange(1,1001):
  s=s+wl(i)
  
print wl(342), wl(111) , wl(200),s