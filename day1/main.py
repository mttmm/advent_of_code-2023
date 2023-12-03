import re
NUMBERS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]


def text_search(line):
    i = 0
    out = False
    while out is False:
        for num in NUMBERS:
            if num in line[0:i]:
                print(line)
                print(num)
            i += 1
            out = str(NUMBERS.index(num) + 1)
    return out









with open("data.txt", 'r') as f:
    text = f.readlines()

ans1 = 0
for line in text:
    line = line.strip()
    digits = (re.findall(r'\d', line))
    ans1 += int(digits[0] + digits[-1])

    #part 2
    new_line = text_search(line)

    # print(new_line)

    # print(digits + num_text)
    # print(num_text)






print(ans1)