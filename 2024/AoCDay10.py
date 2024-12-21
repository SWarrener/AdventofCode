# https://adventofcode.com/2024/day/10


def inbounds(grid, coords):
    if 0 <= coords[0] < len(grid) and 0 <= coords[1] < len(grid[0]):
        return True
    return False


def pathfind(grid, start):
    locations = {start}
    for height in range(1, 10):
        new = set()
        for cy, cx in locations:
            for dy, dx in ((0,-1),(0,1),(1,0),(-1,0)):
                ny, nx = cy + dy, cx + dx
                if inbounds(grid, (ny,nx)) and grid[ny][nx] == height:
                    new.add((ny,nx))
        locations = new
    return len(locations)


with open("input10.txt") as f:
    grid = []
    for line in f.readlines():
        grid.append(list(map(int,line.strip())))

p1_answer = sum(pathfind(grid, (y,x)) for y, line in enumerate(grid) for x, char in enumerate(line) if char == 0)
print(f"The answer to part 1 is {p1_answer}")
p2_answer = 2
print(f"The answer to part 2 is {p2_answer}")
