from puzzle_input import example_input, puzzle_input

CONFIG = 1 # 0 = example input, 1 = puzzle input
INPUT = example_input if CONFIG == 0 else puzzle_input

su = 0

for line_idx, line in enumerate(INPUT.splitlines()):
    if len(line) == 0:
        continue
    # For each number, check if it is adjecant to a symbol
    for char_idx, char in enumerate(line):
        if char != "*":
            continue
        # Search for surrounding numbers
        surroundings_numbers = []
        char_str = ""
        for i in range(line_idx - 1, line_idx + 2):
            for j in range(char_idx - 1, char_idx + 2):
                if i < 0 or i >= len(INPUT.splitlines()):
                    continue
                if j < 0 or j >= len(line):
                    continue
                if i == line_idx and j == char_idx:
                    continue
                if INPUT.splitlines()[i][j].isdigit():
                    char_str = INPUT.splitlines()[i][j]
                    # Continue searching for more numbers
                    # Go left first
                    j_new = j - 1
                    while j_new >= 0 and INPUT.splitlines()[i][j_new].isdigit():
                        char_str = INPUT.splitlines()[i][j_new] + char_str
                        j_new -= 1
                    # Go right
                    j_new = j + 1
                    while j_new < len(line) and INPUT.splitlines()[i][j_new].isdigit():
                        char_str += INPUT.splitlines()[i][j_new]
                        j_new += 1
                    if not int(char_str) in surroundings_numbers:
                        surroundings_numbers.append(int(char_str))
        print("surroundings_numbers:", surroundings_numbers)
        if len(surroundings_numbers) == 2:
            su += surroundings_numbers[0] * surroundings_numbers[1]     
          
print("su:", su)
