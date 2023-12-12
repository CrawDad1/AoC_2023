import regex as re

def checkDice(num: str, color: str)-> bool:
    dice_set = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    
    is_possible = int(num) <= dice_set.get(color, 0)

    print(f"Roll: {num + ' ' + color} | valid?: {is_possible}")
    return is_possible

total = 0
with open("./input.txt", "r") as infile:
    for line in infile:
        possible_game = []
        gameID, roll_string = line.split(':', maxsplit=1)
        rolls = roll_string.split(';')
        print(gameID)
        print(f"Game ID: {gameID.split()[1]}")
        for roll in rolls:
            dice = roll.split(',')
            for die in dice:
                num, color = die.split()
                possible_game.append(checkDice(num, color))
        print(f"Game results: {possible_game}")
        if all(possible_game):
            total = total + int(gameID.split()[1])

print(f"Total: {total}")