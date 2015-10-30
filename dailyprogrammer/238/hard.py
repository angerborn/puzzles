def add_tuples(t1, t2):
    return tuple(x + y for x, y in zip(t1, t2))

with open("challenge_input.txt") as f:
    floors = f.read().split("\n\n")
    floors = [floor.splitlines() for floor in floors]
    map = {
            (x, y, z): c
            for z, floor in enumerate(floors)
            for y, lines in enumerate(floor)
            for x, c in enumerate(lines)
            }

def solve():
    directions = [(0, 1, 0), (1, 0, 0), (0, -1, 0), (-1, 0, 0)]
    up = (0, 0, -1)
    down = (0, 0, 1)
    for pos, c in map.iteritems():
        if c == 'S':
            start = pos
    queue = [start]
    visited = {start: None}
    goal = None
    while queue:
        current = queue.pop(0)
        if current in map:
            c = map[current]
            if c == "G":
                goal = current
                break
            adjacent = []
            if c in " S":
                adjacent = [add_tuples(current, d) for d in directions]
            if c == "U":
                adjacent.append(add_tuples(current, up))
            if c == "D":
                adjacent.append(add_tuples(current, down))
            for new_location in adjacent:
                if new_location not in visited:
                    queue.append(new_location)
                    visited[new_location] = current
    backtrack = goal
    while backtrack:
        if map[backtrack] == " ":
            map[backtrack] = "*"
        backtrack = visited[backtrack]

    for z, floor in enumerate(floors):
        print
        for y, lines in enumerate(floor):
            print "".join([map[(x, y, z)] for x, _ in enumerate(lines)])

solve()
