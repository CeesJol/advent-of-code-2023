from puzzle_input import example_input, puzzle_input

CONFIG = 1 # 0 = example input, 1 = puzzle input
INPUT = example_input if CONFIG == 0 else puzzle_input

prod = 0
times, distances = [], []

for line_idx, line in enumerate(INPUT.splitlines()):
    if len(line) == 0:
        continue
    if line_idx == 0:
        times = line.split(":")[1].split(" ")
        times = list(filter(None, times))
        times = [int(x) for x in times]
    elif line_idx == 1:
        distances = line.split(":")[1].split(" ")
        distances = list(filter(None, distances))
        distances = [int(x) for x in distances]
    else:
        raise Exception("Invalid input")

number_of_ways_to_beat_prod = 1
for time, distance in zip(times, distances):
    number_of_ways_to_beat = 0
    for hold_btn_secs in range(time + 1):
        speed = hold_btn_secs
        travel_time = time - hold_btn_secs
        traveled_distance = speed * travel_time
        if traveled_distance > distance:
            number_of_ways_to_beat += 1
    number_of_ways_to_beat_prod *= number_of_ways_to_beat

print("times:", times)
print("distances:", distances)
print("prod:", number_of_ways_to_beat_prod)
