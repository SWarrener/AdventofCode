#https://adventofcode.com/2023/day/16

# Adds two lists together where A[0] + B[0] = C[0]
def AddList(A, B):
    return [A[i] + B[i] for i in range(0, len(A))]

# Process the beam as it moves around the grid, working out which tiles are have been visited
def ProgressLight(grid, beams):
    visited = set()
    while beams:
        # each beam: [direction of travel, current position]
        beam = beams.pop(0)
        direction = beam[0]
        next_ = AddList(direction, beam[1])
        if next_[0]<0 or next_[0]>=len(grid) or next_[1]<0 or next_[1]>=len(grid): #Grid is a square
            continue
        if (tuple(next_), tuple(direction)) not in visited:
            visited.add((tuple(next_), tuple(direction)))
        else:
            continue
        beam[1] = next_
        next_char = grid[next_[0]][next_[1]]
        if next_char == ".":
            beams.append([direction, next_])
        elif next_char == "\\": #'\'
            beams.append([[direction[1], direction[0]], next_])
        elif next_char == "/":
            beams.append([[direction[1]*-1, direction[0]*-1], next_])
        elif next_char == "-":
            if direction[0] == 0:
                beams.append([direction, next_])
            else:
                beams.append([[0,1], next_])
                beams.append([[0,-1], next_])
        elif next_char == "|":
            if direction[1] == 0:
                beams.append([direction, next_])
            else:
                beams.append([[-1,0], next_])
                beams.append([[1,0], next_])
    return len(set(x[0] for x in visited))

# Extract a list of lists representing the grid
with open("input16.txt") as f:
    grid = []
    for line in f.readlines():
        grid.append(list(line.strip()))

p1answer = ProgressLight(grid, [[[0,1], [0,-1]]])

print(f"The answer to part 1 is: {p1answer}")

p2answer = 0

for i in range(len(grid)):
    p2answer = max(p2answer, ProgressLight(grid, [[[0,1], [i,-1]]]),
                    ProgressLight(grid, [[[0,-1], [i,len(grid)]]]))
    p2answer = max(p2answer, ProgressLight(grid, [[[1,0], [-1,i]]]),
                    ProgressLight(grid, [[[-1,0], [len(grid),i]]]))

print(f"The answer to part 2 is: {p2answer}")
