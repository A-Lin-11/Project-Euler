handle = open("ex13.txt","r")

num = handle.readlines()

s=0
for i in num:
  s = s + int(i)

print str(s)[:10]