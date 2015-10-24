import sys
sys.path.append("../../lib")
import primes

def truncations(number):
    truncations = set()
    divisor = 10
    n = number % divisor
    while number > divisor:
        truncations.add(n)
        divisor = divisor * 10
        n = number % divisor
    n = number / 10
    while n > 0:
        truncations.add(n)
        n = n / 10
    return truncations

limit = 10 ** 6
primes = primes.sieve(limit)
truncatable_primes = set()
for i in xrange(11, limit):
    if primes[i]:
        truncs = truncations(i)
        is_truncatable = True
        while len(truncs) > 0:
            trunc = truncs.pop()
            if not primes[trunc]:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.add(i)
print sum(truncatable_primes)
