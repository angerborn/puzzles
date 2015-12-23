from collections import defaultdict

"""
hlf r sets register r to half its current value, then continues with the next instruction.
tpl r sets register r to triple its current value, then continues with the next instruction.
inc r increments register r, adding 1 to it, then continues with the next instruction.
jmp offset is a jump; it continues with the instruction offset away relative to itself.
jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
"""
out = "b"
p = []
for line in open("input", "r").readlines():
    line = line.strip()
    if line[:2] == "ji":
        # op reg, offset
        op, reg, offset = line.split(" ")
        offset = int(offset)
        reg = reg[0]
    elif line[:3] == "jmp":
        op, offset = line.split(" ")
        offset = int(offset)
        reg = 0
    else:
        op, reg = line.split(" ")
        offset = 0
    p.append((op, reg, offset))

def run(p, a=0):
    r = defaultdict(int)
    r["a"] = a
    ptr = 0
    while ptr < len(p):
        op, reg, offset = p[ptr]
        if op == "hlf":
            r[reg] /= 2
            ptr += 1
        if op == "tpl":
            r[reg] *= 3
            ptr += 1
        if op == "inc":
            r[reg] += 1
            ptr += 1
        if op == "jmp":
            ptr += offset
        if op == "jie":
            if r[reg] % 2 == 0:
                ptr += offset
            else:
                ptr += 1
        if op == "jio":
            if r[reg] == 1:
                ptr += offset
            else:
                ptr += 1
    return r[out]
print "Part 1: {}".format(run(p))
print "Part 2: {}".format(run(p, 1))
