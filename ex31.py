ct = 2

for a in xrange(2):                 #100p
  for b in xrange(5):               #50p
    for c in xrange(11):            #20p
      for d in xrange(21):          #10p
        for e in xrange(41):        #5p
          s = a*100 + b*50 + c*20 + d*10 + e*5
          if s <= 200:
            ct += 1+(200-s)/2
          else:
            continue
print ct