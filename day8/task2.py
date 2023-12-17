from typing import List
from puzzle_input import example_input_task2, puzzle_input

CONFIG = 1 # 0 = example input, 1 = puzzle input
INPUT = example_input_task2 if CONFIG == 0 else puzzle_input

su = 0
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
for i in range(1_000_000_000): # 1_000_000
    if i % 100_000 == 0:
        print(i)
    # Check if all pointers end in Z
    all_pointers_end_in_z = True
    for pointer in pointers:
        # print("pointer.start", pointer.start)
        if pointer.start[-1] != "Z":
            all_pointers_end_in_z = False
            break
    if all_pointers_end_in_z:
        break
    
    # Move pointers
    for instruction in instructions:
        for p_idx, pointer in enumerate(pointers):
            if instruction == "L":
                pointers[p_idx] = map_items[pointer.l]
            elif instruction == "R":
                pointers[p_idx] = map_items[pointer.r]
        su += 1
        # Check if all pointers end in Z
        all_pointers_end_in_z = True
        for pointer in pointers:
            if pointer.start[-1] != "Z":
                all_pointers_end_in_z = False
                break
        if all_pointers_end_in_z:
            break

print(i)
print(len(pointers))
print(len(instructions))
print("su", su)
    
