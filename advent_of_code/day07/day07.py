def extract_operation(string):
    l = string.split(" ")
    # return ((name, in1, in2), outname)
    if len(l) == 3:
        return ("COPY", l[0], ""), l[2]
    elif len(l) == 4:
        return ("NOT", l[1], ""), l[3]
    else:
        return (l[1], l[0], l[2]), l[4]

cache = {}
def find_value(sig):
    # Recursively find value of node
    if sig.isdigit():
        return int(sig)
    if sig in cache:
        return cache[sig]
    name, in1, in2 = ops[sig]
    if name == "COPY":
        result = find_value(in1)
    elif name == "NOT":
        result = ~find_value(in1)
    elif name == "AND":
        result = find_value(in1) & find_value(in2)
    elif name == "OR":
        result = find_value(in1) | find_value(in2)
    elif name == "RSHIFT":
        result = find_value(in1) >> find_value(in2)
    elif name == "LSHIFT":
        result = find_value(in1) << find_value(in2)
    else:
        raise Exception("Unexpected operator {}".format(name))
    cache[sig] = result
    return result

ops = {}
with open("input", "r") as f:
    for line in f.readlines():
        op, out = extract_operation(line.strip())
        ops[out] = op
# part 1
print find_value("a")
# part 2
ops["b"] = ("COPY", "46065", "")
cache = {}
print find_value("a")
