from puzzle_input import example_input, puzzle_input

su = 0

MAX_AMOUNT_RED = 12
MAX_AMOUNT_GREEN = 13
MAX_AMOUNT_BLUE = 14

for line in puzzle_input.splitlines():
    if len(line) == 0:
        continue
    game_id = int(line.split(":")[0].split(" ")[-1])
    game_entries = line.split(":")[1].strip().split(";")
    print(game_id, game_entries)
    min_amount_red, min_amount_green, min_amount_blue = 0, 0, 0
    for game_entry in game_entries:
        grab_entries = game_entry.split(",")
        for grab_entry in grab_entries:
            grab_entry = grab_entry.strip()
            ball_amount = int(grab_entry.split(" ")[0])
            ball_color = grab_entry.split(" ")[1]
            if ball_color == "red":
                min_amount_red = max(min_amount_red, ball_amount)
            elif ball_color == "green":
                min_amount_green = max(min_amount_green, ball_amount)
            elif ball_color == "blue":
                min_amount_blue = max(min_amount_blue, ball_amount)
            else:
                raise Exception(f"Invalid ball color: {ball_color}")
    prod = min_amount_red * min_amount_green * min_amount_blue
    su += prod
          
print("su:", su)
