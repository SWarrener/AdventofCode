# https://adventofcode.com/2024/day/10

# Check if coordinates are in bounds or not
def inbounds(grid, coords):
    if 0 <= coords[0] < len(grid) and 0 <= coords[1] < len(grid[0]):
        return True
    return False

# "Pathfinds" through the grid, moving to all valid tiles that can be reached
def pathfind(grid, start, p1 = False):
    locations = [start]
    for height in range(1, 10):
        new = []
        for cy, cx in locations:
            for dy, dx in ((0,-1),(0,1),(1,0),(-1,0)):
                ny, nx = cy + dy, cx + dx
                if inbounds(grid, (ny,nx)) and grid[ny][nx] == height:
                    new.append((ny,nx))
        locations = new
    if p1:
        return(len(set(locations)))
    return len(locations)

# Extracts a list of lists representing the grid
with open("input10.txt") as f:
    grid = []
    for line in f.readlines():
        grid.append(list(map(int,line.strip())))

p1_answer = sum(pathfind(grid, (y,x), True) for y, line in enumerate(grid) for x, char in enumerate(line) if char == 0)
print(f"The answer to part 1 is {p1_answer}")
p2_answer = sum(pathfind(grid, (y,x)) for y, line in enumerate(grid) for x, char in enumerate(line) if char == 0)
print(f"The answer to part 2 is {p2_answer}")
