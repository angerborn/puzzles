import random
f = {}
for i, line in enumerate(open("secretsantas", "r").readlines()):
    family = line.strip().split(" ")
    f.update({p: i for p in family})

santas = f.keys()

while True:
    random.shuffle(santas)
    assignments = {a: b for a,b in zip(santas, santas[1:] + [santas[0]])}
    if all([f[a] != f[b] for a,b in assignments.iteritems()]):
        break

for a, b in assignments.iteritems():
    print "{} ({})-> {} ({})".format(a, f[a], b, f[b])
