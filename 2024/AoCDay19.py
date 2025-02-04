# https://adventofcode.com/2024/day/19
from functools import cache

# Recursively check the front of each design to see if there is a match
@cache
def check_design(towels, design: str):
    if design == "":
        return True
    for pattern in towels:
        if design.startswith(pattern):
            if check_design(towels, design[len(pattern):]):
                return True
    return False

# Wrapper for check design
def solve_p1(towels, designs):
    for design in designs:
        yield 1 if check_design(towels, design) else 0

# Recursively count number of possible solutions
@cache
def solve_p2(towels, design: str):
    return design == "" or sum(solve_p2(towels, design.removeprefix(pattern))
                               for pattern in towels if design.startswith(pattern))

# Get a list of designs and a list of available towels
with open("input19.txt") as f:
    designs, towels = [], ""
    for i, line in enumerate(f.readlines()):
        if i == 0:
            towels = tuple(line.replace(" ", "").strip().split(","))
        elif line != "\n":
            designs.append(line.strip())

p1_answer = sum(solve_p1(towels, designs))
print(f"The answer to part 1 is {p1_answer}")
p2_answer = sum(solve_p2(towels, design) for design in designs)
print(f"The answer to part 2 is {p2_answer}")
