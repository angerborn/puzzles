# Yes, I modified it to print solution to both part 1 and 2
# after I unlocked part 2.
directions = open("day1.in", "r").read().strip()
level, found = 0, False
for i, direction in enumerate(directions):
    if direction == "(":
        level += 1
    else:
        level -= 1
    if level == -1 and not found:
        print i+1 # part 2
        found = True
print level # part 1
