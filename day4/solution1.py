# Day 4 Question 1
import re

filename = 'day4/input.txt'
cards = []
points = 0

with open(filename, 'r') as f:
    for line in f:
        cards.append(line)

card: str
for card in cards:
    cardID, nums = card.split(':', 1)
    winning_nums, nums = nums.split('|', 1)
    winning_nums = re.findall(r'\d+', winning_nums)
    nums = re.findall(r'\d+', nums)

    match_count = 0
    current_points = 0

    for num in nums:
        if num in winning_nums:
            match_count += 1
    
    if match_count > 0:
        current_points = pow(2, match_count-1)
    
    points += current_points

    print(f"CardID: {cardID} | matches: {match_count}")

print(f"Points: {points}")