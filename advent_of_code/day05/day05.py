import re

def is_string_nice(string):
    """
    A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), 
    or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part 
    of one of the other requirements.
    """
    vowels = "aeiou"
    forbidden = ["ab", "cd", "pq", "xy"]
    vowel_count = 0
    any_appear_twice = False
    last = ""
    for c in string:
        if last + c in forbidden:
            return False
        if last == c and not any_appear_twice:
            any_appear_twice = True
        if c in vowels:
            vowel_count += 1
        last = c
    if any_appear_twice and vowel_count >= 3:
        return True
    return False

def is_super_nice(string):
    """
    Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the 
    string without overlapping, like xyxy (xy) or aabcdefgaa (aa), 
    but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, 
    like xyx, abcdefeghi (efe), or even aaa.
    """
    repeating_pair = r"([a-z][a-z]).*\1"
    repeating_letter = r"([a-z])[a-z]\1"
    if re.search(repeating_pair, string) and re.search(repeating_letter, string):
        return True
    return False

def count_nice(filename, func):
    with open(filename, "r") as f:
        count = 0
        for line in f.readlines():
            string = line.strip()
            if func(string):
                count += 1
        return count



if __name__ == "__main__":
    filename = "day05.in"
    print("Part 1: {}".format(count_nice(filename, is_string_nice)))
    print("Part 2: {}".format(count_nice(filename, is_super_nice)))
