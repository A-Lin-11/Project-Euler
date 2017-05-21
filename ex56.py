m,a,b = 0,0,0

def ds(x):
    l = str(x)
    q = 0
    for i in l:
        q += int(i)
    return q

for i in xrange(2,100):
    for j in xrange(2,100):
        q = ds(i**j)
        if q > m:
            m,a,b = q,i,j

print m
