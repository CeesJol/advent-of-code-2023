from typing import List
import math

from puzzle_input import example_input_task2, puzzle_input

CONFIG = 1 # 0 = example input, 1 = puzzle input
INPUT = example_input_task2 if CONFIG == 0 else puzzle_input

instructions, map_items = "", {}

class MapItem:
    def __init__(self, start, l, r):
        self.start = start
        self.l = l
        self.r = r

    def __str__(self) -> str:
        return f"{self.start} {self.l} {self.r}"

# Parse input
for line_idx, line in enumerate(INPUT.splitlines()):
    if len(line) == 0:
        continue
    if line_idx == 0:
        instructions = line
    else:
        start = line.split(" ")[0].strip()
        l = line.split("(")[1].split(",")[0].strip()
        r = line.split(", ")[1].split(")")[0].strip()
        map_items[start] = MapItem(start, l, r)

pointers: List[MapItem] = []
for map_item_key in map_items:
    map_item = map_items[map_item_key]
    if map_item.start[-1] == "A":
        pointers.append(map_item)

# Repeat instructions until we reach ZZZ
# Move pointers
pointer_lengths = []
for p_idx in range(len(pointers)):
    found = False
    su = 0
    for i in range(10000):
        if found:
            pointer_lengths.append(su)
            break
        for instruction in instructions:
            if instruction == "L":
                pointers[p_idx] = map_items[pointers[p_idx].l]
            elif instruction == "R":
                pointers[p_idx] = map_items[pointers[p_idx].r]
            su += 1
            # Check if pointer ends in Z
            if pointers[p_idx].start[-1] == "Z":
                found = True
                break
            
lcm = pointer_lengths[0]
for i in pointer_lengths[1:]:
    lcm = lcm * i // math.gcd(lcm, i)
print("lcm", lcm)
