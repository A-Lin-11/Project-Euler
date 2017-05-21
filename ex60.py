from itertools import combinations

prime = []

def is_prime(x):
    for i in xrange(2, int(x**0.5)+1):
        if x % i == 0 :
            return False
    return True

n = 20000

for i in xrange (3,n):
    if is_prime(i):
        prime.append(i)

l = len(prime)

prime.pop(1)

def dp(x,y):
    if is_prime(int(str(x)+str(y))) & is_prime(int(str(y)+str(x))):
        return True
    return False


nomatch = True
pt=[]
fa=[]

s = 30000*5
ls=[]
for i in combinations(prime,2):
    if dp(i[0],i[1]):
        ls.append(i)
'''while nomatch == True:
        if q:
            print j, sum(j)
            if sum(j)<s:
                s = sum(j)
                fa = j
    if min(j)>10:
        nomatch = False

print s,fa'''
print len(ls)
