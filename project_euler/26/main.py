def recurring_cycle(n):
	cache = {}
	value = 1
	length = 0
	while not value in cache and value > 0:
		cache[value] = length
		value = (value * 10) % n
		length += 1
	if value in cache:
		return length - cache[value]
	else:
		return 0

def find_max_cycle(d):
	maximum = 0
	maximum_number = 0
	for x in xrange(d, 0, -1):
		if maximum > x:
			break
		length = recurring_cycle(x)
		if maximum < length:
			maximum = length
			maximum_number = x
	if maximum > 0:
		return maximum_number
	return -1

print find_max_cycle(1000)