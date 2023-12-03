from puzzle_input import puzzle_input

su = 0

cur_first_digit, cur_last_digit = None, None

for line in puzzle_input.splitlines():
    print(line)
    for char in line:
        if char.isdigit():
            if cur_first_digit is None:
                cur_first_digit = int(char)
            cur_last_digit = int(char)
    if cur_first_digit is None:
        cur_first_digit, cur_last_digit = None, None
        continue
    num = 10 * cur_first_digit + cur_last_digit
    su += num
    # Reset
    cur_first_digit, cur_last_digit = None, None

print(su)
