# https://adventofcode.com/2023/day/15

# Determines the ASCII code for the string
def CalcHash(string):
    answer = 0
    for code in string.encode('ascii'):
        answer = ((answer + code)*17) % 256
    return answer

# Find where in a box a lens is, returning -1 if it isn't there.
def FindLens(box, string):
    for i, lens in enumerate(box):
        if lens[0] == string:
            return i
    return -1

# Go through the lenses, and remove/replace them from the boxes according to the
# puzzle instructions. Return the list of boxes once the lenses are all where they should be
def solve_p2(boxes, lenses):
    for lens in lenses:
        box_num = CalcHash(lens[0])
        temp = FindLens(boxes[box_num], lens[0])
        if lens[1] == '-':
            if temp != -1:
                boxes[box_num].pop(temp)
        if lens[1] == "=":
            if temp == -1:
                boxes[box_num].append([lens[0], lens[2]])
            else:
                boxes[box_num][temp] = [lens[0], lens[2]]
    return boxes

# extract a list of strings where each string is one part of the puzzle input.
with open("input15.txt") as f:
    for line in f.readlines():
        strings = line.strip().split(",")

p1answer = sum(CalcHash(string) for string in strings)

print(f"The answer to part 1 is: {p1answer}")

# Get a list of lenses, where the lens is the id, the type, and then optionally the focal length
lenses = [[string[:-1], '-'] if '-' in string else
        [string[:string.find('=')], "=", string[-1]] for string in strings]

boxes = [[] for _ in range(256)]

boxes = solve_p2(boxes, lenses)

p2answer = sum((1+i)*(1+j)*int(lens[1]) for i, box in enumerate(boxes) for j, lens in enumerate(box))

print(f"The answer to part 1 is: {p2answer}")
