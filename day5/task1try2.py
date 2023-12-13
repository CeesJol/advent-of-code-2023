from puzzle_input import example_input, puzzle_input

CONFIG = 1 # 0 = example input, 1 = puzzle input
INPUT = example_input if CONFIG == 0 else puzzle_input

seeds, maps = [], []

for line_idx, line in enumerate(INPUT.splitlines()):
    # print(f"line {line_idx}")
    if len(line) == 0:
        continue
    if line_idx == 0:
        seeds = [int(s) for s in line.split()[1:]]
        continue
    
    # Map sentence
    if line[-1] == ":": 
        maps.append([])
        continue
    
    # Must be reading mappings
    destination_range_start, source_range_start, range_length = [int(s) for s in line.split()]
    maps[-1].append({
        "destination_range_start": destination_range_start,
        "source_range_start": source_range_start,
        "range_length": range_length,
    })

seeds_mapped = [seed for seed in seeds]

for seed_idx, seed in enumerate(seeds):
    for map_idx, map in enumerate(maps):
        for range in map:
            # Check if the seed is in the range
            if seeds_mapped[seed_idx] >= range["source_range_start"] and seeds_mapped[seed_idx] < range["source_range_start"] + range["range_length"]:
                # Map the seed
                seeds_mapped[seed_idx] = range["destination_range_start"] + seeds_mapped[seed_idx] - range["source_range_start"]
                # Stop checking ranges: do not map the seed more than once per map
                break
        print(f"map_idx {map_idx}: seed {seed} mapped to {seeds_mapped[seed_idx]}")

min_seed_mapped = min(seeds_mapped)
print("min_seed_mapped", min_seed_mapped)
