#https://adventofcode.com/2023/day/5

# Take a number, run it through the maps. The if statement finds the correct
# set of numbers, and then we calculate the destination number. If the target num is
# equal to itself in this map then it is unchanged by the second for loop.
def find_location_number(targetnum):
    for sets in maps.values():
        for set_ in sets:
            dest, source, modifier = set_
            if source <= targetnum < source + modifier:
                targetnum = dest + (targetnum-source)
                break
    return targetnum

# Take the current ranges and run them through one map. Each range must have one of 5
# relationships with the maps. The range must either fully enlocse, be fully enclosed by,
# or have overlap at the top or bottom, or have no overlap with a set. We find which relationship
# is applicable and map the numbers accordingly, adding the leftover bit of the range
# back into the original loop if applicable.
def find_location_ranges(ranges, key):
    locationranges = []
    for range_ in ranges:
        start, end = range_
        added = False   
        for set_ in maps[key]:
            dest, source, modifier = set_
            source_end = source + modifier
            if start >= source and end < source_end:
                locationranges.append((start - source + dest, end - source + dest))
                added = True
            elif start < source_end <= end and source < start:
                locationranges.append((start - source + dest, source_end - source + dest))
                ranges.append((source_end, end))
                added = True
            elif source >= start and source_end < end:
                locationranges.append((dest, source_end - source + dest))
                added = True
            elif start < source <= end and source_end > end:
                locationranges.append((dest, end - source + dest))
                ranges.append((start, source-1))
                added = True
        if not added:
            locationranges.append((start, end))
    return locationranges

# Open the file and extract a list containing the seeds, and a
# dictionary containing a list of tuples for each map, where each
# tuple is a line of three digits from the input.
with open("input5.txt") as f:
    maps = {}
    for line in f.readlines():
        if "seeds" in line:
            seeds = list(map(int, line[7:-1].split(" ")))
            continue
        if not line[0].isdigit() and line[0] != "\n":
            category = line[:line.find(" ")]
            maps[category] = []
        if line[0].isdigit():
            nums = tuple(map(int, line[:-1].split(" ")))
            maps[category].append(nums)

# Run the function for p1 and print the answer
p1answer = min(find_location_number(seed) for seed in seeds)
print(f"The answer to part 1 is: {p1answer}")

# change the list of seeds to ranges, then run the function for p2 and print the answer
ranges = [(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]

for key in maps:
    ranges = find_location_ranges(ranges, key)
p2answer = min(range[0] for range in ranges)

print(f"The answer to part 2 is: {p2answer}")
