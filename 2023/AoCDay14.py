# https://adventofcode.com/2023/day/14

# Inverts the grid, so  ((1, 2),(3, 4)) becomes ((1, 3),(2, 4))
def InvertGrid(grid):
    return [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]

# Rotate the grid by 90 degrees clockwise so ((1, 2),(3, 4)) becomes ((3, 1),(4, 2))
def RotateGrid90(grid):
    return [list(reversed(x)) for x in zip(*grid)]

# Rolls the moveable rocks towards the top of the grid. Works by inverting the grid and
# moving them to the left (start of each line), then inverting the grid back.
def RollRocks(grid):
    grid = InvertGrid(grid)
    for line in grid:
        last_cube, sphere_count = -1, 0
        for i, item in enumerate(line):
            if item == '.':
                continue
            if item == '#':
                last_cube = i
                sphere_count = 0
            elif item == 'O':
                sphere_count += 1
                line[i] = '.'
                line[last_cube+sphere_count] = 'O'
    grid = InvertGrid(grid)
    return grid

# Calculate the load on the grid
def CalculateLoad(grid):
    load = 0
    for i, line in enumerate(grid):
        load += line.count('O') * (len(grid) - i)
    return load

# Roll rocks 4 times, once in each direction (actually works by always rolling in the same
# direction but rotating the grid each time)
def OneCycle(grid):
    for _ in range(4):
        grid = RollRocks(grid)
        grid = RotateGrid90(grid)
    return grid

# Extracts a list of lists representing the grid
with open("input14.txt") as f:
    grid = []
    for line in f.readlines():
        grid.append(list(line.strip()))

print(f"The answer to part 1 is: {CalculateLoad(RollRocks(grid))}")

# Keeps rolling the rocks until we find a grid pattern that it repeated. Once we have that 
# use some modulo arithmetic to find the answer.
keys = []

while True:
    grid = OneCycle(grid)
    if grid not in keys:
        keys.append(grid)
    else:
        loop_start = keys.index(grid)
        loop = keys[loop_start:]
        p2answer = CalculateLoad(loop[(1000000000-loop_start-1) % len(loop)])
        break

print(f"The answer to part 2 is: {p2answer}")
