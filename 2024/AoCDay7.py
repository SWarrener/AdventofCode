# https://adventofcode.com/2024/day/7

import itertools

# Create a list of operands depending on the part
def create_options(length, p2):
    if p2:
        return list(itertools.product(["*", "+", "|"], repeat=length))
    return list(itertools.product(["*", "+"], repeat=length))

# Using the list of operands, perform the operations in order and see if they create the
# test value, if they do return it and if they don't return 0
def solve(test, nums, p2 = False):
    for option in create_options(len(nums)-1, p2):
        total = nums[0]
        for i in range(1, len(nums)):
            if option[i-1] == "+":
                total += nums[i]
            elif option[i-1] == "*":
                total *= nums[i]
            elif option[i-1] == "|":
                total = int(str(total) + str(nums[i]))
        if total == test:
            return test
    return 0

# Gets a list of tuples of the test value and a list of the other numbers
with open("input7.txt") as f:
    equations = []
    for line in f.readlines():
        answer = int(line[:line.find(":")])
        nums = list(map(int, line[line.find(" "):].strip().split(" ")))
        equations.append((answer, nums))

p1_answer = sum(solve(k, v) for k, v in equations)
p2_answer = sum(solve(k, v, True) for k, v in equations)

print(f"The answer to part 1 is {p1_answer}")
print(f"The answer to part 2 is {p2_answer}")
