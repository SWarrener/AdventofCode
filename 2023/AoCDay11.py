# https://adventofcode.com/2023/day/11

# Find the empty rows and columns. Done by finding the rows, rotating the grid and then
# finding the rows again. Returns a dict of two lists of indicies
def FindEmpty(grid):
    rows = [i for i, line in enumerate(grid) if '#' not in line]
    grid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
    columns = [i for i, line in enumerate(grid) if '#' not in line]
    return {"rows":rows, "columns": columns}

# Returns a list of all of coords of all stars
def FindCoords(grid):
    coords = []
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == '#':
                coords.append((j, i))
    return coords

# Find the distance between each pair of stars, adding in the required number of extra
# rows/columns for each empty column
def CalcDistance(pairs, emptylists, emptyaddition):
    total = 0
    for pair in pairs:
        Ax, Bx, Ay, By = pair[0][0], pair[1][0], pair[0][1], pair[1][1]
        total += abs(Ax - Bx)
        total += abs(Ay - By)
        for i in emptylists["columns"]:
            if Bx < i <Ax or Ax < i < Bx:
                total += emptyaddition
        for i in emptylists["rows"]:
            if By < i <Ay or Ay < i < By:
                total += emptyaddition
    return total

# Extract a list of lists representing the characters in the grid
with open("input11.txt") as f:
    grid = []
    for line in f.readlines():
        grid.append(list(line.strip()))

empty = FindEmpty(grid)
coords = FindCoords(grid)
pairs = [(coords[i], coords[j]) for i in range(len(coords)) for j in range(i+1, len(coords))]

p1answer = CalcDistance(pairs, empty, 1)
print(f"The answer to part 1 is: {p1answer}")

p2answer = CalcDistance(pairs, empty, 999999)
print(f"The answer to part 2 is: {p2answer}")
