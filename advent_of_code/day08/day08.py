string_code_total = 0
string_values_total = 0
string_encoded_total = 0
with open("input", "r") as f:
    for line in f.readlines():
        line = line.strip()
        evalline = eval(line)
        string_code_total += len(line)
        string_values_total += len(evalline)
        string_encoded_total += line.count("\\") + line.count("\"") + 2
print "Part 1: {}".format(string_code_total - string_values_total)
print "Part 2: {}".format(string_encoded_total)
