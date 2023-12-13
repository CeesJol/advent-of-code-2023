from puzzle_input import example_input, puzzle_input

CONFIG = 0 # 0 = example input, 1 = puzzle input
INPUT = example_input if CONFIG == 0 else puzzle_input

seeds = []
highest_found = 0
maps = []

for line_idx, line in enumerate(INPUT.splitlines()):
    print(f"line {line_idx}")
    if len(line) == 0:
        continue
    if line_idx == 0:
        seeds = [int(s) for s in line.split()[1:]]
        continue
    
    # Map sentence
    if line[-1] == ":": 
        maps.append({})
        continue
    
    # Must be reading mappings
    destination_range_start, source_range_start, range_length = [int(s) for s in line.split()]

    for i in range(range_length):
        maps[-1][source_range_start + i] = destination_range_start + i
        highest_found = max(highest_found, source_range_start + i)

    # Find min of maps[-1].keys()
    min_key = min(maps[-1].keys())
    for i in range(min_key):
        maps[-1][i] = i
    max_key = max(maps[-1].keys())
    for i in range(max_key, highest_found + 1):
        maps[-1][i] = i

    # Sort maps[-1] by key
    maps[-1] = dict(sorted(maps[-1].items()))

seeds_mapped = [seed for seed in seeds]

for seed_idx, seed in enumerate(seeds):
    for map in maps:
        if seeds_mapped[seed_idx] in map:
            seeds_mapped[seed_idx] = map[seeds_mapped[seed_idx]]
            print(f"seed {seed} mapped to {seeds_mapped[seed_idx]}")
        else:
            raise Exception(f"seed {seed} not found in map {map}")

print("seeds_mapped after", seeds_mapped)

min_seed_mapped = min(seeds_mapped)
print("min_seed_mapped", min_seed_mapped)
