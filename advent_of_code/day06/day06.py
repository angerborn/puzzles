GRIDSIZE = 1000

def get_instructions():
    instructions = []
    with open("input", "r") as f:
        for line in f.readlines():
            parts = line.split(" ")
            if parts[0] == "toggle":
                action = "toggle"
                start, end = parts[1], parts[3]
            else:
                action = parts[1]
                start, end = parts[2], parts[4]
            start = map(int, start.split(","))
            end = map(int, end.split(","))
            instructions.append((action, start, end))
    return instructions

def bool_lights(instructions):
    grid = [[False] * GRIDSIZE for _ in range(GRIDSIZE)]
    for action, start, end in instructions:
        for x in range(start[0], end[0]+1):
            for y in  range(start[1], end[1]+1):
                if action == "on":
                    grid[x][y] = True
                elif action == "off":
                    grid[x][y] = False
                else:
                    grid[x][y] = not grid[x][y]

    count = 0
    for x in range(GRIDSIZE):
        for y in  range(GRIDSIZE):
            if grid[x][y]:
                count += 1
    return count

def int_lights(instructions):
    grid = [[0] * GRIDSIZE for _ in range(GRIDSIZE)]
    for action, start, end in instructions:
        for x in range(start[0], end[0]+1):
            for y in  range(start[1], end[1]+1):
                if action == "on":
                    grid[x][y] += 1
                elif action == "off":
                    grid[x][y] -= 1
                    if grid[x][y] < 0:
                        grid[x][y] = 0
                else:
                    grid[x][y] += 2

    count = 0
    for x in range(GRIDSIZE):
        for y in  range(GRIDSIZE):
                count += grid[x][y]
    return count

instructions = get_instructions()
print("Part 1: {}".format(bool_lights(instructions)))
print("Part 2: {}".format(int_lights(instructions)))
