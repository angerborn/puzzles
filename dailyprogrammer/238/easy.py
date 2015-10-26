# https://www.reddit.com/r/dailyprogrammer/comments/3q9vpn/20151026_challenge_238_easy_consonants_and_vowels/

from random import choice

def generate_word(pattern):
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    word = [choice(consonants if c in "cC" else vowels) for c in pattern]
    correct_case_word = [upper(c) if oc.isupper() else c for c, oc in zip(word, pattern)]
    return "".join(correct_case_word)

def generate_pattern(length):
    return [choice("cv") for i in range(length)]

for i in range(10):
    print generate_word(generate_pattern(8))
