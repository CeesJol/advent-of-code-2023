from puzzle_input import example_input, puzzle_input

CONFIG = 1 # 0 = example input, 1 = puzzle input
INPUT = example_input if CONFIG == 0 else puzzle_input

su = 0

# Parse input
for line_idx, line in enumerate(INPUT.splitlines()):
    if len(line) == 0:
        continue
    numbers = [int(n) for n in line.split(" ")]

    # Collect sequences: difference between each number
    sequences = [numbers]
    while True:
        cur_sequence = sequences[-1]
        new_sequence = []
        for i in range(len(cur_sequence) - 1):
            new_sequence.append(cur_sequence[i + 1] - cur_sequence[i])
        # Check if new_sequence is zeroes only
        sequences.append(new_sequence)
        if all([n == 0 for n in new_sequence]):
            break
        
    # Append 0 to each sequence and backwards calculate new numbers
    for sequence in sequences:
        sequence.append(0)
    for s_idx in range(len(sequences) - 2, -1, -1):
        sequences[s_idx][-1] = sequences[s_idx][-2] + sequences[s_idx + 1][-1]

    print(sequences)
    su += sequences[0][-1]

print("su", su)
