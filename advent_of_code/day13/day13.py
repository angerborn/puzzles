import re
from collections import defaultdict
from itertools import permutations

happiness = defaultdict(int)
guests = set()

r = r"(\S+) would (lose|gain) (\d+) happiness units by sitting next to (\S+)."
for line in open("input", "r").readlines():
    a, g, v, b = re.findall(r, line)[0]
    v = int(v)
    if g == "lose":
        v = -v
    happiness[(a,b)] += v
    happiness[(b,a)] += v
    guests.add(a), guests.add(b)

# Uncomment in case of part 2
# part2 = True
# if part2:
#     me = "Me"
#     guests.add(me)

best = (0, None)
for arrangement in permutations(guests):
    arrangement = list(arrangement)
    arrangement = zip(arrangement, arrangement[1:] + [arrangement[0]])
    h = sum([happiness[neighbours] for neighbours in arrangement])
    if h > best[0]:
        best = (h, arrangement)
print best[0]

