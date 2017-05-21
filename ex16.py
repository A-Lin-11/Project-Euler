def sod(x):
  s=0
  for i in str(x):
    s = s + int(i)
  return s
  
print sod(2**1000)