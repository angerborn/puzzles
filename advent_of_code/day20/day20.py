goal = 33100000
max_houses = 1000000

# Part 1
# presents = [0] * max_houses
# for i in range(1, max_houses):
#     j = i
#     while j < max_houses:
#         presents[j] += i * 10
#         j += i

# for i, p in enumerate(presents):
#     if p >= goal:
#         print i
#         break

# Part 2
presents = [0] * max_houses
for i in range(1, max_houses):
    j = i
    for _ in range(50):
        if j >= max_houses:
            break
        presents[j] += i * 11
        j += i

for i, p in enumerate(presents):
    if p >= goal:
        print i
        break
