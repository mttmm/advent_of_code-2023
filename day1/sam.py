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


def main():
    # Read the input
    with open("data.txt", "r") as f:
        data = f.readlines()

    # Create the list of values
    values = []
    for line in data:
        print(line)
        line = line.strip()
        first = search(line)
        last = search(line, reverse=True)

        print(f'{first}{last}')
        print("\n--\n")

        values.append(int(f'{first}{last}'))

    print(values)

    # Sum the values
    summed_values = sum(values)

    print(summed_values)


def search(line, reverse=False):
    out = False
    if reverse is False:
        print("Forward")
        i = 0
        while out == False:
            # Check for numeric
            if line[i].isnumeric():
                out = line[i]

            # Check for number words
            for num in NUMBERS:
                if num in line[0:i]:
                    print("Found number")
                    print(num)
                    out = str(NUMBERS.index(num) + 1)

            i += 1

    elif reverse is True:
        print("Reverse")
        i = len(line) - 1
        while out == False:
            # Check for numeric
            if line[i].isnumeric():
                out = line[i]

            # Check for number words
            for num in NUMBERS:
                if num in line[i:]:
                    print("Found number")
                    print(line[-1:i])
                    print(num)
                    out = str(NUMBERS.index(num) + 1)

            i -= 1

    return out


main()