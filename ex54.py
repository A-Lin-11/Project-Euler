def hc(st):
    l=st.split()
    p1,p2,p3,p4,p5 = l[0][0],l[1][0],l[2][0],l[3][0],l[4][0]
    d = {}
    for i in xrange(2,10):
        d[str(i)] = i
    d['T']=10
    d['J']=11
    d['Q']=12
    d['K']=13
    d['A']=14
    cl = [d[p1],d[p2],d[p3],d[p4],d[p5]]
    cl.sort()
    c1,c2,c3,c4,c5 = cl[0],cl[1],cl[2],cl[3],cl[4]
    return [c5,c4,c3,c2,c1]

def pk(st):
    l = st.split()
    s1,s2,s3,s4,s5 = l[0][1],l[1][1],l[2][1],l[3][1],l[4][1]
    cl = hc(st)
    c1,c2,c3,c4,c5 = cl[4],cl[3],cl[2],cl[1],cl[0]

    if s1==s2==s3==s4==s5:
        if c1==c2-1==c3-2==c4-3==c5-4:
            if c1 == 10:
            # Royal Flush
                return 200000
            # Royal Flush
            return 100000 + c1

    if c1==c2==c3==c4:
        # Royal Flush
        return 80000 + c2*50 + c5
    if c2==c3==c4==c5:
        return 80000 + c2*50 + c1

    if c1==c2==c3 and c4==c5:
        # Full House
        return 70000 + c3*50 + c4
    if c5==c4==c3 and c2==c1:
        return 70000 + c3*50 + c1

    if s1==s2==s3==s4==s5:
        # Flush
        return 60000 + c5

    if c1==c2-1==c3-2==c4-3==c5-4:
        # Straight
        return 50000 + c1

    if (c1==c2==c3) or (c4==c2==c3):
        # Three of a Kind
        return 40000 + c3*50 + c5
    if c5==c4==c3:
        return 40000 + c3*50 + c2

    if (c1==c2 and c3==c4) or (c1==c2 and c4==c5) or (c2==c3 and c4==c5):
        # Three of a Kind
        return 30000 + c4*50 + c2

    if c1==c2 or c3==c2:
        # One Pair
        return 15000 + c2*50 + c5
    if c3==c4:
        return 15000 + c4*50 + c5
    if c4==c5:
        return 15000 + c4*50 + c3


    return 10 # One Pair

def poker(str):
    h1 = str[:15]
    h2 = str[15:]
    if pk(h1) > pk(h2):
        return 1
    if pk(h1) < pk(h2):
        return 0
    if pk(h1) == pk(h2):
        if pk(h1) > 10:
            return 'how?'
        else:
            if hc(h1) > hc(h2):
                return 1
            elif hc(h1) < hc(h2):
                return 0
            elif hc(h1) == hc(h2):
                return '??'

f = open('p054_poker.txt','r')
games = f.readlines()
c = []
for i in games:
    c.append(poker(i))
print len(c), sum(c)
