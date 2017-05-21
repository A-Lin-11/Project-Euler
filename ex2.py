eflist = [2]

i=1
j=2

while j<=4000000:
  i,j = j, i+j
  if j%2==0:
    eflist.append (j)
print eflist, sum(eflist)