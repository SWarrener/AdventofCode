# https://adventofcode.com/2024/day/1

# Take each list, sort them and return the absolute value of each item in list 1
# minus its corresponding value in list 2
def solve_part_1(list1: list, list2: list):
    list1, list2 = sorted(list1), sorted(list2)
    for i, val in enumerate(list1):
        yield abs(val - list2[i])


# Take both lists, for every item in list 1 yield the count of that item in list 2
def solve_part_2(list1: list, list2: list):
    for x in list1:
        yield x * list2.count(x)

# Get the two lists of numbers
with open("input1.txt") as f:
    list1, list2 = [], []
    for line in f.readlines():
        list1.append(int(line[:line.find(" ")]))
        list2.append(int(line[line.rfind(" "):]))

p1answer = sum(solve_part_1(list1, list2))
p2answer = sum(solve_part_2(list1, list2))

print(f"The answer to part 1 is: {p1answer}")
print(f"The answer to part 2 is: {p2answer}")
