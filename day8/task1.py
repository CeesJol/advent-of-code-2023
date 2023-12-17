from puzzle_input import example_input, puzzle_input

CONFIG = 1 # 0 = example input, 1 = puzzle input
INPUT = example_input if CONFIG == 0 else puzzle_input

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

pointer: MapItem = map_items["AAA"]

# Repeat instructions until we reach ZZZ
for i in range(1000):
    if pointer.start == "ZZZ":
        break
    for instruction in instructions:
        if instruction == "L":
            pointer = map_items[pointer.l]
        elif instruction == "R":
            pointer = map_items[pointer.r]
        su += 1
        print("pointer", pointer.start)
        if pointer.start == "ZZZ":
            break

print("i", i)
print("su", su)
    
