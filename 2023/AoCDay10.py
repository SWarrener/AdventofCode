# https://adventofcode.com/2023/day/10

import sys, datetime
sys.setrecursionlimit(15000)

# Take two tuples and add each item together to return one tuple
def addtuple(A, B):
    return tuple(A[i] + B[i] for i in range(len(A)))

# Take two tuples and subtract each item in A from B to return one tuple
def subtracttuple(A, B):
    return tuple(A[i] - B[i] for i in range(len(A)))

# Work out which character is hidden under the 'S' in the input, by finding which
# neighbouring characters point at it
def solvestart(coords):
    for k, v in patterns.items():
        correct = 0
        for set_ in v:
            new = addtuple(coords, set_)
            newchar = matrix[new[1]][new[0]]
            if newchar == '.':
                continue
            temp = patterns[newchar].copy()
            if (set_[0]*-1, set_[1]*-1) in temp:
                correct += 1
        if correct == 2:
            return k
    return None

# For each step and the move to your current positions and find the character at your
# new position, look it up in the patterns list and remove the direction you've just
# come from from the move options. Then call recursively with the new data. Return
# length of the loop when done
def domove(move, cur):
    loop.append(cur)
    new = addtuple(move, cur)
    newchar = matrix[new[1]][new[0]]
    if newchar == "S":
        return None
    temp = patterns[newchar].copy()
    temp.remove((move[0]*-1, move[1]*-1))
    return domove(temp[0], new)

# Take a position and the position you came from and work out which directions are
# left and right from your current location. Return these directions
def findLandR(coords, prevcoords):
    headdirection = subtracttuple(prevcoords, coords)
    if headdirection[0] == 0:
        left = (headdirection[1],0)
        right = (headdirection[1]*-1,0)
    elif headdirection[1] == 0:
        left = (0,headdirection[0]*-1)
        right = (0,headdirection[0])
    return [left, right]

# Progress around the loop, looking to the left and right each time, once you have found
# the edge of the matrix without hitting the loop return the other direction. This points
# towards the inside of the loop.
def findinside():
    for idx, cur in enumerate(loop):
        dirs = findLandR(cur, loop[idx-1])
        finL, finR = False, False
        new = cur
        while not finL:
            new = addtuple(new, dirs[0])
            if new[0] >= 140 or new[0] < 0 or new[1] >= 140 or new[1] < 0:
                return "R"
            if new in loop:
                finL = True
        new = cur
        while not finR:
            new = addtuple(new, dirs[1])
            if new[0] >= 140 or new[0] < 0 or new[1] >= 140 or new[1] < 0:
                return "L"
            if new in loop:
                finR = True
    return None

# When looking inside the loop, the corner characters need to look in two directions, this
# transforms one direction into the other
def transformrel(char, rel):
    if char in ("7", "L"):
        return (rel[1]*-1, rel[0]*-1)
    if char in ("J", "F"):
        return (rel[1], rel[0])
    return None

# Goes round the loop, looking inside for each tile, counting the number of tiles fully
# enclosed within the loop. returns that number
def countinside(dir_):
    inside = set()
    for idx, cur in enumerate(loop):
        dirs = findLandR(cur, loop[idx-1])
        if dir_ == "L":
            rel = dirs[0]
        elif dir_ =="R":
            rel = dirs[1]
        new = cur
        while (new := addtuple(new, rel)) not in loop:
            inside.add(new)
        if matrix[cur[1]][cur[0]] in ["7", "L", "J", "F"]:
            rel = transformrel(matrix[cur[1]][cur[0]], rel)
            new = cur
            while (new := addtuple(new, rel)) not in loop:
                inside.add(new)
    return len(inside)

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

startchar = solvestart(start)
domove(patterns[startchar][0], start)
p1answer = int(len(loop)/2)
print(f"The answer to part 1 is: {p1answer}")

first = datetime.datetime.now()
p2answer = countinside(findinside())
print(datetime.datetime.now()-first)
print(f"The answer to part 2 is: {p2answer}")
