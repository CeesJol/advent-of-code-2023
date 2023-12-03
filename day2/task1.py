from puzzle_input import example_input, puzzle_input

su = 0

MAX_AMOUNT_RED = 12
MAX_AMOUNT_GREEN = 13
MAX_AMOUNT_BLUE = 14

for line in puzzle_input.splitlines():
    line_is_valid = True
    if len(line) == 0:
        continue
    # print(line)
    game_id = int(line.split(":")[0].split(" ")[-1])
    game_entries = line.split(":")[1].strip().split(";")
    print(game_id, game_entries)
    for game_entry in game_entries:
        grab_entries = game_entry.split(",")
        cur_amount_red, cur_amount_green, cur_amount_blue = 0, 0, 0
        for grab_entry in grab_entries:
            grab_entry = grab_entry.strip()
            ball_amount = int(grab_entry.split(" ")[0])
            ball_color = grab_entry.split(" ")[1]
            if ball_color == "red":
                cur_amount_red += ball_amount
            elif ball_color == "green":
                cur_amount_green += ball_amount
            elif ball_color == "blue":
                cur_amount_blue += ball_amount
            else:
                raise Exception(f"Invalid ball color: {ball_color}")
            if cur_amount_red > MAX_AMOUNT_RED:
                print(f"Game {game_id} has too many red balls")
                line_is_valid = False
                break
            if cur_amount_green > MAX_AMOUNT_GREEN:
                print(f"Game {game_id} has too many green balls")
                line_is_valid = False
                break
            if cur_amount_blue > MAX_AMOUNT_BLUE:
                print(f"Game {game_id} has too many blue balls")
                line_is_valid = False
                break
    if line_is_valid:
        su += game_id
          
print("sum:", su)




