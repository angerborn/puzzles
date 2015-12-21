from collections import defaultdict

# Set to False for part 1, True fort part 2
part2 = True

def add(t1, t2):
    return tuple(x + y for x, y in zip(t1, t2))

grid = defaultdict(bool)
for y, line in enumerate(open("input", "r").readlines()):
    for x, c in enumerate(line):
        if c == "#":
            grid[(x,y)] = True
        else:
            grid[(x,y)] = False
active = 0
dirs = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
for i in range(100):
    grid_copy = defaultdict(bool)
    active = 0
    corners = [(0,0), (0,99), (99,99), (99,0)]
    if part2:
        grid[(0,0)] = True
        grid[(0,99)] = True
        grid[(99,99)] = True
        grid[(99,0)] = True
        active +=4
    for y in range(100):
        for x in range(100):
            current = (x, y)
            if part2 and current in corners:
                continue
            active_neighbours = 0
            for d in dirs:
                neighbour = add(current, d)
                if grid[neighbour]:
                    active_neighbours += 1
            if grid[current] and 2 <= active_neighbours <= 3:
                grid_copy[current] = True
                active += 1
            elif not grid[current] and active_neighbours == 3:
                grid_copy[current] = True
                active += 1
    grid = grid_copy
print active
