handle = open("ex42.txt","r")

w = handle.read().split(",")

tr = []

m = 100
for i in xrange(m):
  tr.append(i*(i+1)/2)

def ws(word):
  s=0
  for i in word[1:-1]:
    s += ord(i)-64
  return s

ct = 0  
for i in w:
  if ws(i) in tr:
    ct += 1
print ct