from hashlib import md5

key = "bgvyzdsv"

def solve(zeroes):
    for i in range(100000000):
        digest = md5((key + str(i)).encode()).hexdigest()
        if digest[:zeroes] == "0"*zeroes:
            return i

if __name__ == "__main__":
    print("Part 1: {}".format(solve(5)))
    print("Part 2: {}".format(solve(6)))
