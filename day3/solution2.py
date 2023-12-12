# day3 question 2
import  re

matrix = []
gear_map = {}
total = 0
filename = './input.txt'

with open(filename, 'r') as infile:
    for line in infile:
        matrix.append(line.strip())


line: str
for i, line in enumerate(matrix):
    matches = re.finditer(r'\*', line)

    # build map
    for m in matches:
        gear_map[(i,m.start())] = []

for i, line in enumerate(matrix):
    matches = re.finditer(r'\d+', line)

    # check if surrounding coordinates in map
    for m in matches:
        for x in range(i-1, i+2):
            for y in range(m.start()-1,m.end()+1):
                if (x, y) in gear_map:
                    gear_map[(x,y)].append(int(m.group()))
        
for nums in gear_map.values():
    if len(nums) == 2:
        # multiply and add to total
        total += (nums[0] * nums[1])


print(f"Grand Total: {total}")