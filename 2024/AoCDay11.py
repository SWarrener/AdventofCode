# https://adventofcode.com/2024/day/1

# Add stones to the new dictionary, creating a new key if it does not already exist
def add_stones(new, stone, count):
    if stone not in new:
        new[stone] = count
    else:
        new[stone] += count

# For each loop take the stones and what happens to each one, as order is utterly irrelevant
# and the same thing happens to each stone we can just keep track of how many of each stone there
# are
def process_stones(stones: dict, blinks):
    for _ in range(0, blinks):
        new = {}
        for stone in stones:
            if stone == 0:
                add_stones(new, 1, stones[stone])
            elif len(str(stone)) % 2 == 0:
                strstone = str(stone)
                add_stones(new, int(strstone[:int(len(strstone)/2)]), stones[stone])
                add_stones(new, int(strstone[int(len(strstone)/2):]), stones[stone])
            else:
                add_stones(new, stone*2024, stones[stone])
        stones = new
    return sum(count for count in stones.values())

with open("input11.txt") as f:
    for line in f.readlines():
        data = list(map(int, line.strip().split(" ")))

stones = {}
for stone in data:
    add_stones(stones, stone, 1)

p1_answer = process_stones(stones, 25)
print(f"The answer to part 1 is {p1_answer}")
p2_answer = process_stones(stones, 75)
print(f"The answer to part 2 is {p2_answer}")
