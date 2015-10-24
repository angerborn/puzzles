def sieve(limit):
    """ Implementation of erathostenes sieve,
    seems to handle up to 10**7 pretty well """
    limit = limit # expand by one because list index starts at 0
    numbers = [True] * limit
    numbers[0] = numbers[1] = False
    for i in xrange(2, limit):
        if numbers[i]:
            for j in xrange(i*i, limit, i):
                numbers[j] = False
    return numbers

def below(limit):
    primelist = sieve(limit)
    return [i for i in xrange(2, limit) if primelist[i]]
