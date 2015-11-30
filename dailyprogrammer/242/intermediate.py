import sys
filename = sys.argv[1]

shows = []
with open(filename) as f:
    for line in f.readlines():
        start, end, name = line.split(" ", 2)
        shows.append((int(start), int(end), name.strip()))

shows.sort(key = lambda t: t[1])
start, end = 0, 0
recorded = []
for show in shows:
    if show[0] >= end:
        recorded.append(show)
        start, end, _ = show
print recorded
print len(recorded)
