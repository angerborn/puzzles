eps = 0.00000001
for i in range(10, 100):
	for j in range(i, 100):
		if i == j:
			continue
		if j / 10 != i % 10:
			continue
		i2 = int(str(i)[:1])
		j2 = int(str(j)[1:])
		if i2 == 0 or j2 == 0:
			continue
		quot = float(i) / float(j) 
		quot2 = float(i2) / float(j2) 
		if abs(quot - quot2) < eps:
			print i2, j2
