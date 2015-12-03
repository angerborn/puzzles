from itertools import cycle

def houses_visited(santacount, directions):
    """
        Takes the amount of santas and the list of directions,
        returns a map with entries like this {(x, y): number_of_visits}
    """

    moves = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}
    visited = {(0, 0): 1}
    santas = [(0,0)] * santacount
    for santanumber, direction in zip(cycle(range(santacount)), directions):
        move = moves[direction]
        current = santas[santanumber]
        current = (current[0] + move[0], current[1] + move[1])
        visited[current] = visited.get(current, 0) + 1
        santas[santanumber] = current
    return visited

with open("data/day3.in", "r") as f:
    elf_directions = f.read().strip()
print len(houses_visited(1, elf_directions)) # part 1
print len(houses_visited(2, elf_directions)) # part 2
