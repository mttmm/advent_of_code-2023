import re
NUMBERS = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}


def text_search(line):
        for key, value in NUMBERS.items():
            if key in line:
                line = line.replace(key,str(value))
        return line


with open("D:\\projects\\advent-of-code\\day1\\data.txt", 'r') as f:
    text = f.readlines()

ans1 = 0
ans2 = 0

for line in text:
    line = line.strip()
    digits = (re.findall(r'\d', line))
    ans1 += int(digits[0] + digits[-1])

    #part 2
    line = text_search(line)
    digits = (re.findall(r'\d', line))
    ans2 += int(digits[0] + digits[-1])
    # print(new_line)

    # print(digits + num_text)
    # print(num_text)



print(ans1) #54390

print(ans2) # 54277 #



