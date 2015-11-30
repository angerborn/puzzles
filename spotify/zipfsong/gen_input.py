import random
import sys
import string

def generate(n, m):
    print n, m
    for i in range(n):
        print random.randint(0, 10**12),
        print "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 25)))

if __name__ == "__main__":
    n, m = int(sys.argv[1]), int(sys.argv[2])
    generate(n, m)


