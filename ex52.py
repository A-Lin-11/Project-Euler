def pm(x):
	l = []
	for i in str(x):
		l.append(i)
	return set(l)

x = 1
while True:
	x += 1
	if pm(x) == pm(x * 2):
		if pm(x) == pm(x * 3):
			if pm(x) == pm(x * 4):
				if pm(x) == pm(x * 5):
					if pm(x) == pm(x * 6):
						print x
						break
