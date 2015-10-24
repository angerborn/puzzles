words = open("enable1.txt", "r").read().splitlines()

def find_longest(subset):
    longest = ""
    for word in words:
        possible = True
        if len(word) < len(longest):
            continue
        for c in word:
            if c not in subset:
                possible = False
                break
        if possible:
            longest = word
    print longest

lines = int(raw_input())
for _ in range(lines):
    subset = raw_input()
    find_longest(subset)
