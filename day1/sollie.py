import re
a1 = 0
a2 = 0
NUM_STR = ["zero", "one", "two", "three", "four", "five", "six", "seven","eight","nine", "ten"]
#NUM_INT = list(range(0,11)) # This Should work, but they have some dumb shared letters, and I'm to lazy for solve for that soooo
NUM_INT = ["z0o", "o1e", "t2o", "t3e", "f4r", "f5e", "s6x", "s7n","e8t","n9e", "t10n"]

def sub_text(line):
    i = 0
    while i < len(NUM_STR):
        line = re.sub(NUM_STR[i], str(NUM_INT[i]), line)
        i += 1
    return line

with open('D:\\projects\\advent-of-code\\day1\\data.txt') as f:
    for line in f:
        #Part 1
        n = re.sub("\D", "", line)
        a1 += int(n[0] + n[-1])

        #Part 2
        line = sub_text(line)
        n = re.sub("\D", "", line)
        a2 += int(n[0] + n[-1])

#Part 1
print(a1)

#Part 2
print(a2)