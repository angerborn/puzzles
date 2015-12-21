import re
from functools import reduce
import operator

def mult(t1, d):
    return [x * d for x in t1]

def add(l):
    return [sum(li) if sum(li) > 0 else 0 for li in zip(*l)]

def calculate(i, ingredient_counts):
    total = add([mult(x, d) for x, d in zip(i, ingredient_counts)])
    return reduce(operator.mul, total[:-1], 1), total[-1]

r = r"\S+: \S+ (-?\d+), \S+ (-?\d+), \S+ (-?\d+), \S+ (-?\d+), \S+ (-?\d+)"
ingredients = []
for ingredient in re.findall(r, open("input", "r").read()):
    ingredients.append(map(int, ingredient))

best = 0
for i in range(100):
    for j in range(100 - i):
        for k in range(100 - i - j):
            l = 100 - i - j - k
            value, calories = calculate(ingredients, [i, j, k, l])
            # Remove the "and calories == 500" part if solving part 1
            if value > best and calories == 500:
                best = value
print best
