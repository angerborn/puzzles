import re
# part 1
fin = open("input", "r").read()
num_re = r"(-?\d+)"
print sum(map(int, re.findall(num_re, fin)))

from json import loads
d = loads(fin)
def get_value(json):
    if isinstance(json, int):
        return json
    if isinstance(json, basestring):
        return 0
    elif isinstance(json, list):
        sum = 0
        for e in json:
            sum += get_value(e)
        return sum
    elif isinstance(json, dict):
        if "red" in json.values():
            return 0
        sum = 0
        for k, v in json.iteritems():
            sum += get_value(v)
        return sum

print get_value(d)



