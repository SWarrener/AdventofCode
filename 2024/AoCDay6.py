# https://adventofcode.com/2024/day/6
directions = [(-1,0),(0,1),(1,0),(0,-1)]

# Adds two tuples together where A[0] + B[0] = C[0]
def add_tuple(A, B):
    return tuple(A[i] + B[i] for i in range(0, len(A)))

# Subtracts two tuples together where A[0] - B[0] = C[0]
def sub_tuple(A, B):
    return tuple(A[i] - B[i] for i in range(0, len(A)))

# Checks if a positions is in bounds on a square grid
def inbounds(pos, grid):
    y,x = pos
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

# Moves the guard and records the location and direction won't mark the final tile
def walk(cur, grid, dir_ = 0):
    visited = []
    while inbounds(pos := add_tuple(cur, directions[dir_%4]), grid):
        y,x = pos
        if grid[y][x] == "#":
            pos = sub_tuple(pos, directions[dir_%4])
            dir_ += 1
            pos = add_tuple(pos, directions[dir_%4])
        visited.append((cur, dir_))
        cur = pos
    return visited

# Adds up all the unique positions in visited
def calc_p1(visited):
    return len(set(x[0] for x in visited)) + 1

# Finds the "^" which indicates the start
def find_start(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "^":
                return (y, x)
    return None

# Gets a list of lists representing the grid
with open("input6.txt") as f:
    grid = []
    for line in f.readlines():
        grid.append(list(line.strip()))

start = find_start(grid)
visited = walk(start, grid)
p1answer = calc_p1(visited)

print(f"The answer to part 1 is: {p1answer}")
