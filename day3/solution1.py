# day3 question 1
import re

matrix = []
symbol_map = set()
total = 0
filename = './input.txt'

with open(filename, 'r') as infile:
    for line in infile:
        matrix.append(line.strip())


line: str
for i, line in enumerate(matrix):
    matches = re.finditer(r'[^\d\.]', line)
    for m in matches:
        symbol_map.add((i, m.start()))
    
for i, line in enumerate(matrix):
    matches = re.finditer(r'\d+', line)

    for m in matches:
        for x in range(i-1, i+2):
            for y in range(m.start()-1, m.end()+1):
                if (x, y) in symbol_map:
                    total += int(m.group())

   
print(f"Grand Total: {total}")