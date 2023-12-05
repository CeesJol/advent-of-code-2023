from puzzle_input import example_input, puzzle_input

CONFIG = 1 # 0 = example input, 1 = puzzle input
INPUT = example_input if CONFIG == 0 else puzzle_input

su = 0

for line_idx, line in enumerate(INPUT.splitlines()):
    if len(line) == 0:
        continue
    score = 0
    card_idx = line.split(":")[0].split(" ")[1]
    winning_numbers = line.split(":")[1].split("|")[0].strip().split(" ")
    winning_numbers = list(filter(None, winning_numbers))
    winning_numbers = {int(x) for x in winning_numbers}
    my_numbers = line.split(":")[1].split("|")[1].strip().split(" ")
    my_numbers = list(filter(None, my_numbers))
    my_numbers = [int(x) for x in my_numbers]
    for my_number in my_numbers:
        if my_number in winning_numbers:
            score = 1 if score == 0 else score * 2
    su += score
    print(card_idx, winning_numbers, my_numbers, score)
          
print("su:", su)
