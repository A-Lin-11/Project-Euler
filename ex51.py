def is_prime(x):
    for i in xrange(2, int(x**0.5)+1):
        if x % i == 0 :
            return False
    return True

def dr(x):
    for i in xrange(3):
        if str(x).count(str(i)) == 3:
            return i
    return False

def pdf(x):
    l=[]
    if dr(x) is not False:
        for i in xrange(10):
            l.append(int(str(x).replace(str(dr(x)),str(i))))
        return l
    return None

i = 10001
while True:
    if is_prime(i):
        if dr(i) is not False:
            l = pdf(i)
            c = 0
            for p in l:
                if is_prime(p) and p>10000:
                    c += 1
            if c == 8:
                print i
                break
    i += 2

for m in pdf(i):
    print m, is_prime(m)
