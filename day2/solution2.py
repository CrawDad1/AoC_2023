total = 0
with open("./input.txt", "r") as infile:
    for line in infile:
        color_lists = {
            'red': [],
            'blue': [],
            'green': []
        }
        gameID, roll_string = line.split(':', maxsplit=1)
        rolls = roll_string.split(';')
        print(gameID)
        print(f"Game ID: {gameID.split()[1]}")
        for roll in rolls:
            dice = roll.split(',')
            for die in dice:
                num, color = die.split()
                color_lists[color].append(int(num))
        
        print(line)
        print(color_lists)
        print(f"""
              max rolls:
              red:{max(color_lists['red'])}
              blue:{max(color_lists['blue'])}
              green:{max(color_lists['green'])}
              """)
        total = total + (
            max(color_lists['red']) *
            max(color_lists['blue']) *
            max(color_lists['green'])
        )

print(f"Total: {total}")