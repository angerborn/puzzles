from functools import reduce
import operator

last = None
sizes = []
with open("grid2", "r") as f:
    f.readline()
    for i, line in enumerate(f.readlines()):
        x = line.find("X")
        xr = line.rfind("X")
        if x > -1:
            if last:
                sizes.append((last[0] - xr, i - last[1]))
            last = (x, i)

def count(x, y):
    if x == 0 or y == 0:
        return 1
    return count(x-1, y) + count(x, y-1) + count(x-1, y-1)

print reduce(operator.mul, [count(x, y) for x, y in sizes], 1)
