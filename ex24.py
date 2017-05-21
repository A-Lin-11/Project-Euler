from itertools import permutations

a = permutations(xrange(10))

b = list(a)

print b[10**6-1]