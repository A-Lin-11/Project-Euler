from itertools import permutations 

l = []
for i in range(10):
  l.append(str(i))
  
s = 0
for i in permutations(l,10):
  n = ''.join(i)
  if int(n[3])%2==0:
    if int(n[2:5])%3==0:
      if int(n[5])%5==0:
        if int(n[4:7])%7==0:
          if int(n[5:8])%11==0:
            if int(n[6:9])%13==0:
              if int(n[7:10])%17==0:
                s += int(n)
print(s)