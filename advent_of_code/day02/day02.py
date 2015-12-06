def paper_for_dimensions(l, w, h):
    shortest, middle, _ = sorted([l, w, h])
    return 2*(l*w + l*h + w*h) + shortest*middle

def ribbon_for_dimensions(l, w, h):
    shortest, middle, _ = sorted([l, w, h])
    smallest_perimeter = 2 * (shortest + middle)
    volume = l * w * h
    return smallest_perimeter + volume

paper = 0
ribbon = 0
with open("input", "r") as f:
    for line in f.readlines():
        l, w, h = map(int, line.split("x"))
        paper += paper_for_dimensions(l, w, h)
        ribbon += ribbon_for_dimensions(l, w, h)
    print paper
    print ribbon
