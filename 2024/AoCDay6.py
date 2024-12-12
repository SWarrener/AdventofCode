# https://adventofcode.com/2024/day/6
directions = [(-1,0),(0,1),(1,0),(0,-1)]

# Adds two tuples together where A[0] + B[0] = C[0]
def add_tuple(A, B):
    return tuple(A[i] + B[i] for i in range(0, len(A)))

# Checks if a positions is in bounds on a square grid
def inbounds(pos, grid):
    y,x = pos
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

# Takes a step, turning and trying again it we hit an obstacle
def step(cur, dir_, extra = None):
    npos = add_tuple(cur,directions[dir_%4])
    y,x = npos
    if inbounds(npos, grid) and grid[y][x] == "#" or npos == extra:
        dir_ += 1
        return step(cur, dir_, extra)
    return npos, dir_

# Moves the guard and records the location and direction.
def walk(cur, grid, extra = None):
    visited = set()
    dir_ = 0
    while inbounds(cur, grid):
        if (cur, dir_%4) in visited:
            return "loop"
        visited.add((cur, dir_%4))
        cur, dir_ = step(cur, dir_, extra)
    return set(x[0] for x in visited)

# Finds the "^" which indicates the start
def find_start(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "^":
                return (y, x)
    return None

# Put an obstacle at each point in the path and see if it forms a loop
def solve_p2(visited, grid):
    for loc in visited:
        if walk(start, grid, loc) == "loop":
            yield 1

# Gets a list of lists representing the grid
with open("input6.txt") as f:
    grid = []
    for line in f.readlines():
        grid.append(list(line.strip()))

start = find_start(grid)
visited = walk(start, grid)
p1answer = len(visited)
p2answer = sum(solve_p2(visited, grid))

print(f"The answer to part 1 is: {p1answer}")
print(f"The answer to part 2 is: {p2answer}")
