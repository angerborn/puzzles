import random

def matching(password, guess):
    return sum([1 if p == g else 0 for p, g in zip(password, guess)])

def get_words(length, n, filename="../../lib/enable1.txt"):
    with open(filename, "r") as f:
        words = [word for word in map(str.strip, f.readlines()) if len(word) == length]
        return random.sample(words, n)

def clamp(n, nmin, nmax):
    return max(nmin, min(nmax, n))

def fallout_game():
    difficulty = int(raw_input("Difficulty (1-5)? "))
    difficulty = clamp(difficulty, 0, 5)
    word_length = random.choice(((), (4, 5), (6, 7), (8, 9), (10, 11, 12), (13, 14, 15))[difficulty])
    word_amount = random.choice(((), (5, 6), (7, 8), (9, 10), (11, 12, 13), (13, 14, 15))[difficulty])
    words = get_words(word_length, word_amount)
    password = random.choice(words)
    for i, word in enumerate(words):
        print "{} \t {}".format(i, word)
    for n in xrange(4, 0, -1):
        guess = int(raw_input("Guess ({} left)? ".format(n)))
        guess = clamp(guess, 0, word_amount)
        matches = matching(password, words[guess])
        print "{}/{} correct".format(matches, word_length)
        if  words[guess] == password:
            print "You win!"
            break
    else:
        print "You lose!"
    print "The password was {}".format(password)

fallout_game()
