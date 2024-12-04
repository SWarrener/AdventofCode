# https://adventofcode.com/2024/day/3
import re

# Find all regex matches in the string and return the sum of the multiplications
def solve(string: str):
    multiples = re.findall(r"mul\([0-9]*?,[0-9]*?\)", string)
    return sum(int(x[x.find("(")+1:x.find(",")])*int(x[x.find(",")+1:x.find(")")]) for x in multiples)

# Split the string on "don't()", then within these substrings append everything after the
# first "do()" to a result string and put that through the p1 solution.
def solvep2(string):
    result = ""
    substrs = string.split("don't()")
    for sub in substrs:
        match = re.search(r"do\(\)", sub)
        if match:
            result += sub[match.start():]
    return solve(result)


# Removes all the new lines and places entire input in one string
with open("input3.txt") as f:
    string = "do()" # Makes p2 easier
    for line in f.readlines():
        string += line.strip()

p1answer = solve(string)
p2answer = solvep2(string)


print(f"The answer to part 1 is: {p1answer}")
print(f"The answer to path 2 is: {p2answer}")
