from puzzle_input import example_input_task2, puzzle_input

su = 0

cur_first_digit, cur_last_digit = None, None

number_strings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
number_string_to_number = {number_string: idx for idx, number_string in enumerate(number_strings)}

for line in puzzle_input.splitlines():
    print(line)
    for char_idx, char in enumerate(line):
        if char.isdigit():
            if cur_first_digit is None:
                cur_first_digit = int(char)
            cur_last_digit = int(char)
        elif char.isalpha():
            for number_string in number_strings:
                if number_string.startswith(char):
                    for char_idx2, char2 in enumerate(number_string):
                        if char_idx2 == 0:
                            continue
                        if char_idx + char_idx2 >= len(line):
                            break
                        if line[char_idx + char_idx2] != char2:
                            break
                    else:
                        # We found a match
                        if cur_first_digit is None:
                            cur_first_digit = number_string_to_number[number_string]
                        cur_last_digit = number_string_to_number[number_string]
    if cur_first_digit is None:
        cur_first_digit, cur_last_digit = None, None
        continue
    num = 10 * cur_first_digit + cur_last_digit
    su += num
    # Reset
    cur_first_digit, cur_last_digit = None, None

print(su)
