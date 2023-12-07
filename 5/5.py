"""
The almanac (your puzzle input) lists all of the seeds that need to be planted.
It also lists what type of soil to use with each kind of seed, what type of
fertilizer to use with each kind of soil, what type of water to use with each
kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on
is identified with a number, but numbers are reused by each category - that is,
soil 123 and fertilizer 123 aren't necessarily related to each other.

almanac.txt

#format:
map type:
dest_range_start source_range_start range_length

seed-to-soil map:
50 98 2

seed number 98 corresponds to
soil number 50

seed number 99 corresponds to
soil number 51

seed-to-soil map:
52 50 48

destination(soil) range starting at 52
    and also containing 48 values: 52, 53, ..., 98, 99.
source(seed) range starts at 50
    and contains 48 values: 50, 51, ..., 96, 97.
So, seed number 53 corresponds to soil number 55.

###

The almanac starts by listing which seeds need to be planted:
seeds 79, 14, 55, and 13.

The rest of the almanac contains a list of maps which describe how to convert
numbers from a source category into numbers in a destination category. That is,
the section that starts with seed-to-soil map: describes how to convert a seed
number (the source) to a soil number (the destination). This lets the gardener and
his team know which soil to use with which seeds, which water to use with which
fertilizer, and so on.

Rather than list every source number and its corresponding destination number one
by one, the maps describe entire ranges of numbers that can be converted. Each line
within a map contains three numbers: the destination range start, the source range
start, and the range length.

Consider again the example seed-to-soil map:

50 98 2
52 50 48
The first line has a destination range start of 50, a source range start of 98,
and a range length of 2. This line means that the source range starts at 98 and
contains two values: 98 and 99. The destination range is the same length, but it
starts at 50, so its two values are 50 and 51. With this information, you know
that seed number 98 corresponds to soil number 50 and that seed number 99
corresponds to soil number 51.

The second line means that the source range starts at 50 and contains 48 values:
50, 51, ..., 96, 97. This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53 corresponds to soil number 55.

Any source numbers that aren't mapped correspond to the same destination number. So,
seed number 10 corresponds to soil number 10.
"""
from collections import defaultdict

# What is the lowest location number that corresponds to any of the initial seed numbers?

# filename = "almanac.txt"
filename = "input.txt"

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




soils = map(mapper(almanach['seed-to-soil']), seeds)
fertilizers = map(mapper(almanach['soil-to-fertilizer']), soils)
waters = map(mapper(almanach['fertilizer-to-water']), fertilizers)
lights = map(mapper(almanach['water-to-light']), waters)
temps = map(mapper(almanach['light-to-temperature']), lights)
humidities = map(mapper(almanach['temperature-to-humidity']), temps)
locations = map(mapper(almanach['humidity-to-location']), humidities)

l = [l for l in locations]
print(min(l))
