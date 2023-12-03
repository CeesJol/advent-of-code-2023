from puzzle_input import example_input, puzzle_input

CONFIG = 1 # 0 = example input, 1 = puzzle input
INPUT = example_input if CONFIG == 0 else puzzle_input

su = 0

def is_symbol(char: str) -> bool:
    """Returns True if char is a symbol, False otherwise."""
    symbols = "!@#$%^&*()-_=+[{]}\|;:'\",<>/?"
    return char in symbols

for line_idx, line in enumerate(INPUT.splitlines()):
    if len(line) == 0:
        continue
    # For each number, check if it is adjecant to a symbol
    char_start_idx, char_str = 0, ""
    for char_idx, char in enumerate(line):
        if char.isdigit():
            char_str += char
            if char_start_idx == 0:
                # This is the first digit of the number
                char_start_idx = char_idx
            # Check if next char is also a digit
            if (char_idx + 1 < len(line) and line[char_idx + 1].isdigit()):
                continue
            # This is the last digit of the number
            symbol_is_found = False
            for i in range(line_idx - 1, line_idx + 2):
                for j in range(char_start_idx - 1, char_idx + 2):
                    if i < 0 or i >= len(INPUT.splitlines()):
                        continue
                    if j < 0 or j >= len(line):
                        continue
                    if i == line_idx and j == char_idx:
                        continue
                    if is_symbol(INPUT.splitlines()[i][j]):
                        symbol_is_found = True
                        break
            if symbol_is_found:
                su += int(char_str)
            # Reset
            char_start_idx, char_str = 0, ""
          
print("su:", su)
