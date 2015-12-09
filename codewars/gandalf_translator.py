def tongues(code):
    from string import maketrans
    vowels = "aiyeou"
    consonants = "bkxznhdcwgpvjqtsrlmf"
    vowels_rotated = vowels[3:] + vowels[:3]
    consonants_rotated = consonants[10:] + consonants[:10]
    original = vowels + vowels.upper() + consonants + consonants.upper()
    rotated = vowels_rotated + vowels_rotated.upper() + consonants_rotated + consonants_rotated.upper()
    table = maketrans(original, rotated)
    return code.translate(table)

print tongues("Ita dotf ni dyca nsaw ecc.")
