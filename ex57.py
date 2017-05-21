def nd(x):
    return len(str(x))

c = 0
m = 0
i,j = 1,1
while c < 1000:
    i,j =  i+2*j, i+j
    if nd(i) > nd(j):
        m+=1
    c+=1
print m
