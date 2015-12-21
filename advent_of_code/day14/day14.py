import re

time = 2503
furthest = 0
r = r"(\S+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
# Part 1
for name, kms, s, rest in re.findall(r, open("input", "r").read()):
    kms, s, rest = map(int, (kms, s, rest))
    whole = time / (s + rest)
    part =  time % (s + rest)
    part = min(part, s)
    distance = whole * s * kms + part * kms
    if distance > furthest:
        furthest = distance
print "Part 1: {}".format(furthest)

# Part 2
deers = []
for name, v, s, rest in re.findall(r, open("input", "r").read()):
    v, s, rest = map(int, (v, s, rest))
    deers.append({"n": name, "v": v, "s": s, "r": rest, "c": 0, "p": 0, "km": 0})
for s in range(time):
    for deer in deers:
        if deer["c"] < 0:
            deer["c"] += 1
        elif 0 <= deer["c"] < deer["s"]:
            deer["c"] += 1
            deer["km"] += deer["v"]
            if deer["c"] == deer["s"]:
                deer["c"] = -deer["r"]
    furthest = max(deers, key=lambda d: d["km"])
    furthest["p"] += 1
furthest = max(deers, key=lambda d: d["km"])
print "Part 2: {}".format(furthest["p"])
