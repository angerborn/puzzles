import string
import itertools
import re

alpha = string.ascii_lowercase
trans = {x: y for x, y in zip(alpha[-1] + alpha[:-1], alpha)}

def valid(p):
    """
    Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
    Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
    Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
    """
    if "i" in p or "o" in p or "l" in p:
        return False
    if len(re.findall(r"([a-z])\1", p)) < 2:
        return False
    for i, _ in enumerate(p[:-2]):
        s = p[i:i+3]
        if s in alpha:
            return True


def inc(s):
    s = list(s)
    for i, c in reversed(list(enumerate(s))):
        cn = trans[c]
        s[i] = cn
        if c != "z":
            break
    return "".join(s)

def next_password(p):
    while True:
        p = inc(p)
        if valid(p):
            return p

santapass = "cqjxjnds"
nextp = next_password(santapass)
print nextp
print next_password(nextp)
