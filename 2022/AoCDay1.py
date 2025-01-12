# https://adventofcode.com/2022/day/1

# Finds the three highest items in the list and returns their sum
def top_three(elves: list):
    total = 0
    for _ in range(3):
        temp = max(elves)
        del elves[elves.index(temp)]
        total += temp
    return total

# Gets a list of ints of the total calories for each elf
with open("input1.txt") as f:
    elves = []
    total = 0
    for line in f.readlines():
        if line == "\n":
            elves.append(total)
            total = 0
        else:
            total += int(line.strip())

p1_answer = max(elves)
print(f"The answer to part 1 is {p1_answer}")

p2_answer = top_three(elves)
print(f"The answer to part 2 is {p2_answer}")
