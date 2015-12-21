from itertools import combinations

containers = [11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3]
size = 150

total_count = 0
minimum_containers = len(containers)
total_min = 0
for i in range(1, len(containers) + 1):
    for c in combinations(containers, i):
        if sum(c) == size:
            total_count += 1
            if i <= minimum_containers:
                minimum_containers = i
                total_min += 1
print "Part 1: {}".format(total_count)
print "Part 2: {}".format(total_min)
