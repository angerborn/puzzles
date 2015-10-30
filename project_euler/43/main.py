import itertools

def m(l, n):
    return (l[0] * 100 + l[1] * 10 + l[2]) % n != 0

ok_numbers = []
for p in itertools.permutations(range(0,10)):
    if m(p[1:4], 2):
        continue
    if m(p[2:5], 3):
        continue
    if m(p[3:6], 5):
        continue
    if m(p[4:7], 7):
        continue
    if m(p[5:8], 11):
        continue
    if m(p[6:9], 13):
        continue
    if m(p[7:10], 17):
        continue
    ok_numbers.append(int("".join(map(str,p))))
print sum(ok_numbers)
