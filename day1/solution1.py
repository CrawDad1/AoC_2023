# Day One - Question One

# create a two digit number from the first and last digit of a given string
# then add that 2-digit number to a running total
# the answer is the grand total

first = ''
last = ''
total = 0

with open("./input.txt", "r") as infile:
    for line in infile:
        # get first digit
        char: str
        for char in line:
            if char.isdigit():
                first = char
                break
        
        if not (first):
            first = "0"

        for char in reversed(line):
            if char.isdigit():
                last = char
                break 

        if not (last):
            last = "0"

        total = total + int(first + last)
        # print line and results 
        print("************")
        print(line)
        print(first + last)
        print(f"total: {total}")
        print("************")
        

print(f"grand total: {total}")