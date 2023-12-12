# now numbers can be a digit OR a word
# using regex might be the way to go. 

import regex as re

first = ""
last = ""
total = 0

def convertDigit(input: str) -> str:
    num_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    if input.isdigit():
        return input
    else:
        return num_dict.get(input, '0')


with open("./input.txt", "r") as infile:
    for line in infile:
        matches = re.findall('\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
        first = convertDigit(matches[0])
        last = convertDigit(matches[-1])
        total = total + int(first+last)

        print("*************")
        print(line)
        print(matches[0] + " " + matches[-1])
        print(first + last)
        print("*************")

print(f"grand total: {total}")