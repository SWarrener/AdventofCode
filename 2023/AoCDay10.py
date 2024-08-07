import sys
sys.setrecursionlimit(15000)

def addtuple(A, B):
    return tuple([A[i] + B[i] for i in range(0, len(A))])

def subtracttuple(A, B):
    return tuple([A[i] - B[i] for i in range(0, len(A))])

def solvestart(coords):
    for k, v in patterns.items():
        correct = 0
        for set in v:
            new = addtuple(coords, set)
            newchar = matrix[new[1]][new[0]]
            if newchar == '.':
                continue
            temp = patterns[newchar].copy()
            if (set[0]*-1, set[1]*-1) in temp:
                correct += 1
        if correct == 2:
            return k

def domove(move, cur, steps):
    steps += 1
    loop.append(cur)
    new = addtuple(move, cur)
    newchar = matrix[new[1]][new[0]]
    if newchar == "S":
        return steps
    temp = patterns[newchar].copy()
    temp.remove((move[0]*-1, move[1]*-1))
    return domove(temp[0], new, steps)

def findLandR(coords, prevcoords):
    headdirection = subtracttuple(prevcoords, coords)
    if headdirection[0] == 0:
        Left = (headdirection[1],0)
        Right = (headdirection[1]*-1,0)
    elif headdirection[1] == 0:
        Left = (0,headdirection[0]*-1)
        Right = (0,headdirection[0])
    return [Left, Right]

def findinside():
    for i, cur in enumerate(loop):
        dirs = findLandR(cur, loop[i-1])
        finL = False
        finR = False
        new = cur
        while not finL:
            new = addtuple(new, dirs[0])
            if new[0] >= 140 or new[0] < 0 or new[1] >= 140 or new[1] < 0:
                return "R"
            elif new in loop:
                finL = True
        new = cur
        while not finR:
            new = addtuple(new, dirs[1])
            if new[0] >= 140 or new[0] < 0 or new[1] >= 140 or new[1] < 0:
                return "L"
            elif new in loop:
                finR = True

def transformrel(char, rel):
    if char == "7" or char == "L":
        return (rel[1]*-1, rel[0]*-1)
    elif char == "J" or char == "F":
        return (rel[1], rel[0])

def countinside(dir):
    inside = []
    count = 0
    for i, cur in enumerate(loop):
        dirs = findLandR(cur, loop[i-1])
        if dir == "L":
            rel = dirs[0]
        elif dir =="R":
            rel = dirs[1]
        new = cur
        while True:
            new = addtuple(new, rel)
            if new in loop:
                break
            if new not in inside:
                count += 1
                inside.append(new)
        if matrix[cur[1]][cur[0]] in ["7", "L", "J", "F"]:
            rel = transformrel(matrix[cur[1]][cur[0]], rel)
            new = cur
            while True:
                new = addtuple(new, rel)
                if new in loop:
                    break
                if new not in inside:
                    count += 1
                    inside.append(new)
    return count

patterns = {"J": [(-1, 0), (0, -1)], "F": [(1, 0), (0, 1)], "|": [(0, -1), (0, 1)], 
            "-": [(-1, 0), (1, 0)], "L": [(1, 0), (0, -1)], "7": [(0, 1), (-1, 0)],}

loop = []

with open("input10.txt") as f:
    matrix = []
    for line in f.readlines():
        matrix.append(list(line.strip()))

for i,row in enumerate(matrix):
    if "S" in row:
        start = (row.index("S"), i)

startchar = solvestart(start)
p1answer = int(domove(patterns[startchar][0], start, 0)/2)

print(f"The answer to part 1 is: {p1answer}")

p2answer = countinside(findinside())

print(f"The answer to part 2 is: {p2answer}")
