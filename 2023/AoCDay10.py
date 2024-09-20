# https://adventofcode.com/2023/day/10
import sys
from shapely.geometry import Polygon

sys.setrecursionlimit(15000)

# Take two tuples and add each item together to return one tuple
def add_tuple(A, B):
    return tuple(A[i] + B[i] for i in range(len(A)))

# Work out which character is hidden under the 'S' in the input, by finding which
# neighbouring characters point at it
def solve_start(coords):
    for k, v in patterns.items():
        correct = 0
        for set_ in v:
            new = add_tuple(coords, set_)
            new_char = matrix[new[1]][new[0]]
            if new_char == '.':
                continue
            temp = patterns[new_char].copy()
            if (set_[0]*-1, set_[1]*-1) in temp:
                correct += 1
        if correct == 2:
            return k
    return None

# For each step and the move to your current positions and find the character at your
# new position, look it up in the patterns list and remove the direction you've just
# come from from the move options. Then call recursively with the new data. Return
# length of the loop when done
def do_move(move, cur):
    loop.append(cur)
    new = add_tuple(move, cur)
    new_char = matrix[new[1]][new[0]]
    if new_char == "S":
        return None
    temp = patterns[new_char].copy()
    temp.remove((move[0]*-1, move[1]*-1))
    return do_move(temp[0], new)

# Find every corner in the loop, done by subtracting the coords of idx-1 from idx+1 and
# multiplying them, and then taking the absolute value. An answer of 2 means the coords
# at idx are not a corner, and an answer of 1 means they are. Create a polygon using these
# corners, and then subtract half the length from the area and add 1 to find the number of
# interior tiles.
def count_inside(loop):
    corners = [coords for i, coords in enumerate(loop) if
               abs((loop[i-1][0]-loop[(i+1)%len(loop)][0])
                   * (loop[i-1][1]-loop[(i+1)%len(loop)][1])) == 1]
    shape = Polygon(corners)
    return int(shape.area - shape.length/2 + 1)


patterns = {"J": [(-1, 0), (0, -1)], "F": [(1, 0), (0, 1)], "|": [(0, -1), (0, 1)],
            "-": [(-1, 0), (1, 0)], "L": [(1, 0), (0, -1)], "7": [(0, 1), (-1, 0)],}

loop = []

# Extract a list of lists representing the characters in the grid.
with open("input10.txt") as f:
    matrix = []
    for line in f.readlines():
        matrix.append(list(line.strip()))

for i,row in enumerate(matrix):
    if "S" in row:
        start = (row.index("S"), i)

start_char = solve_start(start)
do_move(patterns[start_char][0], start)
p1answer = int(len(loop)/2)
print(f"The answer to part 1 is: {p1answer}")

p2answer = count_inside(loop)
print(f"The answer to part 2 is: {p2answer}")
