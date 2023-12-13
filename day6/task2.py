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
    
time, distance = "", ""
for time_, distance_ in zip(times, distances):
    time += str(time_)
    distance += str(distance_)
time, distance = int(time), int(distance)

print("time:", time)
print("distance:", distance)

# Linear O(n)
# number_of_ways_to_beat = 0
# for hold_btn_secs in range(time + 1):
#     if hold_btn_secs % 10000 == 0:
#         print("hold_btn_secs:", hold_btn_secs)
#     speed = hold_btn_secs
#     travel_time = time - hold_btn_secs
#     traveled_distance = speed * travel_time
#     if traveled_distance > distance:
#         print(f"{hold_btn_secs} beats the distance")
#         number_of_ways_to_beat += 1

# Binary search O(log n)
# Find lowest value that beat the distance
low, high = 0, time
number_of_ways_to_beat_low = 0
while low <= high:
    mid = (low + high) // 2
    speed = mid
    travel_time = time - mid
    traveled_distance = speed * travel_time
    if traveled_distance > distance:
        number_of_ways_to_beat_low = mid
        high = mid - 1
    else:
        low = mid + 1

print("number_of_ways_to_beat_low", number_of_ways_to_beat_low)

# Find highest value that beat the distance
low, high = 0, time
number_of_ways_to_beat_high = 0
while low <= high:
    mid = (low + high) // 2
    speed = mid
    travel_time = time - mid
    traveled_distance = speed * travel_time
    if traveled_distance > distance:
        number_of_ways_to_beat_high = mid
        low = mid + 1
    else:
        high = mid - 1

print("low", low)
print("high", high)
print("prod:", number_of_ways_to_beat_high - number_of_ways_to_beat_low + 1)
