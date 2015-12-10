def is_merge(s, part1, part2):
    """ Checks if s is a merge of part1 and part2 """
    if len(s + part1 + part2) == 0:
        return True
    if not part1:
        return s == part2
    if not part2:
        return s == part1
    if not s:
        return False
    if len(part1 + part2) != len(s):
        return False
    if s[0] == part1[0] and is_merge(s[1:], part1[1:], part2):
        return True
    if s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]):
        return True
    return False