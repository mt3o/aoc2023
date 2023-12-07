filename = "almanac.txt"
# filename = "input.txt"

with open(filename) as f:
    seeds = [int(num) for num in f.readline().strip().split(" ")[1:]]
    f.readline()  # empty line
    almanach = {}
    all_lines = f.readlines()
    pointer = 0
    while pointer < len(all_lines):
        line = all_lines[pointer]
        pointer += 1
        type = line.split(" ")[0]
        almanach[type] = []
        while pointer < len(all_lines):
            line = all_lines[pointer]
            pointer += 1
            if line == "\n":
                break
            almanach[type].append([int(num) for num in line.strip().split(" ")])


def mapper(listing):

    l = sorted(listing, key=lambda x: x[1])
    lowest = l[0][1]
    highest = l[-1][1] + l[-1][2]
    def map(number):
        if number < lowest:
            return number
        if number > highest:
            return number
        for dest,source,range in l:
            if source <= number < source+range:
                delta = number - source
                return dest + delta
        return number
    return map


def find_overlap(range1, range2):
    r1_start, r1_end = range1
    r2_start, r2_end = range2
    region_start = max(r1_start, r2_start)
    region_end = min(r1_end, r2_end)
    return (region_start, region_end) if region_start <= region_end else None

def new_seeds():
    groups = []
    for group_start, group_length in zip(seeds[::2],seeds[1::2]):
        groups.append( (group_start, group_start+group_length-1))
    return groups


mappers = [
    mapper(almanach['seed-to-soil']),
    mapper(almanach['soil-to-fertilizer']),
    mapper(almanach['fertilizer-to-water']),
    mapper(almanach['water-to-light']),
    mapper(almanach['light-to-temperature']),
    mapper(almanach['temperature-to-humidity']),
    mapper(almanach['humidity-to-location']),
]


ranges = new_seeds()
for mapper in mappers:
    new_ranges = []
    for r1 in ranges:
        for r2 in ranges:
            if overlap := find_overlap(r1, r2):

                if r1==r2:
                    new_ranges.append((mapper(r1[0]), mapper(r1[1])))
                    break
                if r1[0] > r2[0]:
                    r1, r2 = r2, r1

                overlap_region_start, overlap_region_end = overlap

                new_ranges.append((mapper(r1[0]), mapper(overlap_region_start)))
                new_ranges.append((mapper(overlap_region_start),mapper(overlap_region_end)))
                new_ranges.append((mapper(overlap_region_end), mapper(r2[1])))
                break
        else:
            new_ranges.append((mapper(r1[0]), mapper(r1[1])))
    ranges = new_ranges

print(min([min(start,end) for start,end in ranges]))
