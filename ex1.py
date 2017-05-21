lst=list()

for i in range(1000):
  if i%3 != 0 and i%5 !=0:
    continue
  else:
    lst.append(i)
print sum(lst)