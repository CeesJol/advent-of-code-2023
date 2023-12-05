from puzzle_input import example_input, puzzle_input

CONFIG = 1 # 0 = example input, 1 = puzzle input
INPUT = example_input if CONFIG == 0 else puzzle_input

su = 0
copies = [1 for _ in range(len(INPUT.splitlines()))]

for line_idx, line in enumerate(INPUT.splitlines()):
    if len(line) == 0:
        continue
    copy_idx = line_idx + 1
    card_idx = line.split(":")[0].split(" ")[1]
    winning_numbers = line.split(":")[1].split("|")[0].strip().split(" ")
    winning_numbers = list(filter(None, winning_numbers))
    winning_numbers = {int(x) for x in winning_numbers}
    my_numbers = line.split(":")[1].split("|")[1].strip().split(" ")
    my_numbers = list(filter(None, my_numbers))
    my_numbers = [int(x) for x in my_numbers]
    for my_number in my_numbers:
        if my_number in winning_numbers:
            copies[copy_idx] += copies[line_idx]
            copy_idx += 1
    print(card_idx, winning_numbers, my_numbers)
          
# Sum up the copies
su = 0
for copy in copies:
    su += copy
print("su:", su)
