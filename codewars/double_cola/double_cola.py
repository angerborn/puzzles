import math

def whoIsNext(names, r):
    count = len(names)
    offset = 0
    for i in range(10000):
        sequence_length = count * 2 ** i
        new_offset = offset + sequence_length
        if new_offset > r:
            position = int(math.ceil(float(r - offset) / sequence_length * count) - 1)
            return names[position]
        else:
            offset = new_offset
    return -1
