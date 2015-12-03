import sys
from collections import defaultdict

fruits = []
with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        name, price = line.split(" ")
        fruits.append((name, int(price)))
    fruits.sort(key=lambda fruit: fruit[1], reverse = True)

def solve(index, money):
    if money < 0 or len(fruits) <= index:
        return []
    if money == 0:
        return [defaultdict(int)]
    fruit, price = fruits[index]
    take = solve(index, money - price)
    leave = solve(index+1, money)
    for shoppinglist in take:
        shoppinglist[fruit] += 1
    return take + leave

def print_combo(fruitcombo):
    fruitstrings = []
    for key, value in fruitcombo.iteritems():
        keystring = key if value == 1 else key + "s"
        fruitstrings.append("{1} {0}".format(keystring, value))
    print(", ".join(fruitstrings))

fruits_to_buy = solve(0, 500)
for fruitcombo in fruits_to_buy:
    print_combo(fruitcombo)
