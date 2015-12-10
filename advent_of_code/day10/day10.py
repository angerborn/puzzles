from itertools import groupby

start = "1113222113"

def lookandsay(string):
    return "".join([str(len(list(v))) + k for k, v in groupby(string)])

part1 = start
for _ in range(40):
    part1 = lookandsay(part1)
part2 = start
for _ in range(50):
    part2 = lookandsay(part2)
print "Part 1: {}".format(len(part1))
print "Part 2: {}".format(len(part2))
