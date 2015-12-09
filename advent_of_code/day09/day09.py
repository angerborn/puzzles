import re
import itertools

"""
Solves both parts of the problem by force.
Generates all possible paths with itertools.permutations and calculates distance.
"""

distances = {}
towns = set()
for line in open("input", "r"):
    a, b, d = re.match("(\S+) to (\S+) = (\d+)", line).groups()
    towns.add(a), towns.add(b)
    distances[(a,b)] = distances[(b,a)] = int(d)
shortest_distance, shortest_route = sum(distances.values()), ()
longest_distance, longest_route = 0, ()
for route in itertools.permutations(towns):
    distance = 0
    paths = zip(route, route[1:])
    distance = sum([distances[path] for path in paths])
    if distance < shortest_distance:
        shortest_distance, shortest_route = distance, route
    if distance > longest_distance:
        longest_distance, longest_route = distance, route
print "Part 1: {}".format(shortest_distance)
print "Part 2: {}".format(longest_distance)
