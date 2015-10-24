import itertools

import sys
sys.path.append("../../lib")
import primes

ps = primes.below(10 ** 6)
largest_found = 0
# NOTE: numbers with digits 1..8 & 1..9 are always divisible by 3
# so only necessary to try up to 7 digits.
# Read more: https://en.wikipedia.org/wiki/Divisibility_rule
for permutation in itertools.permutations(range(1, 8)):
    permutation_int = int("".join(map(str, permutation)))
    is_prime = True
    for prime in ps:
        if prime ** 2 >= permutation_int:
            break
        if permutation_int % prime == 0:
            is_prime = False
            break
    if is_prime:
        if largest_found < permutation_int:
            largest_found = permutation_int
print largest_found
