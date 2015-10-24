# https://www.reddit.com/r/dailyprogrammer/comments/3opin7/20151014_challenge_236_intermediate_fibonacciish/

def fib_seq(maxvalue, f1=1):
    last = 0
    sequence = [last]
    current = f1
    while current <= maxvalue:
        yield current
        last, current = current, last + current


def find_multiplier(num):
    multiplier = -1
    for i in fib_seq(num):
        if num % i == 0:
            multiplier = num / i
    return multiplier


def solve(num):
    sequence = list(fib_seq(num, find_multiplier(num)))
    sequence.insert(0, 0)
    return sequence
