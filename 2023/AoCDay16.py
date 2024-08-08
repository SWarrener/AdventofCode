def AddList(A, B):
    return [A[i] + B[i] for i in range(0, len(A))]

def ProgressLight(grid, beams):
    visited = set()
    while beams:
        # each beam: [direction of travel, current position]
        beam = beams.pop(0)
        next = AddList(beam[0], beam[1])
        if next[0]<0 or next[0]>=len(grid) or next[1]<0 or next[1]>=len(grid): #Grid is a square
            continue
        if (tuple(next), tuple(beam[0])) not in visited:
            visited.add((tuple(next), tuple(beam[0])))
        else: continue
        beam[1] = next
        next_char = grid[next[0]][next[1]]
        if next_char == ".":
            beams.append([beam[0], next])
        elif next_char == "\\": #'\'
            beams.append([[beam[0][1], beam[0][0]], next])
        elif next_char == "/":
            beams.append([[beam[0][1]*-1, beam[0][0]*-1], next])
        elif next_char == "-":
            if beam[0][0] == 0: 
                beams.append([beam[0], next])
            else:
                beams.append([[0,1], next])
                beams.append([[0,-1], next])
        elif next_char == "|":
            if beam[0][1] == 0: 
                beams.append([beam[0], next])
            else: 
                beams.append([[-1,0], next])
                beams.append([[1,0], next])
    return len(set([x[0] for x in visited]))

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
