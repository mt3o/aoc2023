with open("input.txt") as f:
    inputs, *transforms = f.read().split("\n\n")

inputs = list(map(int, inputs.split(":")[1].split()))

seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

for transform in transforms:
    transformation_ranges = []
    for single_transform in transform.splitlines()[1:]:
        transformation_ranges.append(list(map(int, single_transform.split())))
    new = []
    while len(seeds) > 0:
        seed_region_start, seed_region_end = seeds.pop()
        for dest, source, length in transformation_ranges:
            overlap_start = max(seed_region_start, source)
            overlap_end = min(seed_region_end, source + length)
            if overlap_start < overlap_end:
                new.append((overlap_start - source + dest, overlap_end - source + dest))
                if overlap_start > seed_region_start:
                    seeds.append((seed_region_start, overlap_start))
                if seed_region_end > overlap_end:
                    seeds.append((overlap_end, seed_region_end))
                break
        else:
            new.append((seed_region_start, seed_region_end))
    seeds = new

print(min(seeds)[0])
