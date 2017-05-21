handle = open("ex11.txt","r")

txt = handle.readlines()

g = []

for i in xrange(20):
  j=txt[i].split()
  for p in xrange(20):
    j[p]=int(j[p])
  g.append(j)

def rt(x,y):
  try:
    return g[x][y] * g[x+1][y] * g[x+2][y] * g[x+3][y]
  except:
    return 1

def dw(x,y):
  try:
    return g[x][y] * g[x][y+1] * g[x][y+2] * g[x][y+3]
  except:
    return 1
    
def rd(x,y):
  try:
    return g[x][y] * g[x+1][y+1] * g[x+2][y+2] * g[x+3][y+3]
  except:
    return 1  
    
def ru(x,y):
  try:
    return g[x][y] * g[x-1][y+1] * g[x-2][y+2] * g[x-3][y+3]
  except:
    return 1  

def mp(x,y):
  return max(rt(x,y),dw(x,y),rd(x,y),ru(x,y))

aws = 0

for i in xrange(20):
  for j in xrange(20):
    if mp(i,j) > aws:
      aws = mp (i,j)

print aws