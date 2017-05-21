from math import factorial

def c(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

print c(23,10)

ct = 0
for i in xrange(23,101):
    for j in xrange(3,i):
        if c(i,j) > 1000000:
            print i,j,c(i,j)
            ct += 1


print ct
