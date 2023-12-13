# Day 4 Question 2
import re

filename = 'day4/input.txt'
card_dict = {}
cards = []
points = 0

with open(filename, 'r') as f:
    for line in f:
        cards.append(line)

# build dict
for id, card in enumerate(cards):
    card_dict[id] = 1

card: str
for id, card in enumerate(cards):
    cardID, nums = card.split(':', 1)
    winning_nums, nums = nums.split('|', 1)
    winning_nums = re.findall(r'\d+', winning_nums)
    nums = re.findall(r'\d+', nums)

    match_count = 0
    for num in nums:
        if num in winning_nums:
            match_count += 1
    
    # distribute copies
    for j in range(1, match_count+1):
        card_dict[id + j] += card_dict[id]


    print(f"CardID: {cardID}| copies: {card_dict[id]} | matches: {match_count}")

total_cards = 0
for value in card_dict.values():
    total_cards += value

print(f"Total cards: {total_cards}")