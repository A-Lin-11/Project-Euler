def sp(i):
    return [i**2-(i-1),i**2-(i-1)*2,i**2-(i-1)*3]

def is_prime(x):
    for i in xrange(2, int(x**0.5)+1):
        if x % i == 0 :
            return 0
    return 1

w = 1.0
i = 1
t = 1.0
p = 0
while w > 0.1:
    i += 2
    t += 4
    for x in sp(i):
        p += is_prime(x)
    w = p / t

print i,w
