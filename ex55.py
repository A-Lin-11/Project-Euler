def pl(x):
    if str(x) == str(x)[::-1]:
        return True
    return False

c=0
r = 10000
for i in xrange(r):
    it = 0
    while it < 50:
        if pl(i+int(str(i)[::-1])):
            c += 1
            break
        else:
            it += 1
            i = i+int(str(i)[::-1])

print r-c
