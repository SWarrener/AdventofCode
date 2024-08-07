def InvertGrid(grid):
    return [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]

def RotateGrid90(grid):
    return [list(reversed(x)) for x in zip(*grid)]

def RollRocks(grid):
    grid = InvertGrid(grid)
    for line in grid:
        last_cube, sphere_count = -1, 0
        for i, item in enumerate(line):
            if item == '.':
                continue
            elif item == '#':
                last_cube = i
                sphere_count = 0
            elif item == 'O':
                sphere_count += 1
                line[i] = '.'
                line[last_cube+sphere_count] = 'O'
    grid = InvertGrid(grid)
    return grid

def CalculateLoad(grid):
    load = 0
    for i, line in enumerate(grid):
        load += line.count('O') * (len(grid) - i)
    return load

def OneCycle(grid):
    for i in range(4):
        grid = RollRocks(grid)
        grid = RotateGrid90(grid)
    return grid

with open("input14.txt") as f:
    grid = []
    for line in f.readlines():
        grid.append(list(line.strip()))

print(f"The answer to part 1 is: {CalculateLoad(RollRocks(grid))}")

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