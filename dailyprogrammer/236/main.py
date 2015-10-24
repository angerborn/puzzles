from random import shuffle

def get_bag():
    pieces = list("OISZLJT")
    shuffle(pieces)
    return pieces

seq = []
for _ in range(8):
    seq += get_bag()

print "".join(seq[:50])
