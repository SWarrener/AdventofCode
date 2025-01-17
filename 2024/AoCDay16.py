# https://adventofcode.com/2024/day/16
import heapq
import copy

# Solves p1 and p2 in the same pass. Pathfinds through the grid to find the lowest scoring route.
# For all routes with that score combine their paths and turn it into a set to get how many tiles
# all those routes combined cross
def pathfind(grid, loc, dir_ = (0,1), speed = -1, tiles = []):
    open_list = [(0, *loc, dir_, [])]
    closed_list = set()
    while True:
        score, cy, cx, dir_, path = heapq.heappop(open_list)
        path.append((cy,cx))
        if (cy, cx) == end and speed == -1:
            speed = score
        if speed == score and (cy, cx) == end:
            tiles += path
            continue
        if score > speed and speed != -1:
            break
        closed_list.add((cy, cx, dir_))
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = dy+cy, dx+cx
            if grid[ny][nx] == "#" or (ny, nx, (dy, dx)) in closed_list:
                continue
            cost = 1001 if (dy,dx) != dir_ else 1
            heapq.heappush(open_list, (score+cost, ny, nx, (dy, dx), copy.copy(path)))
    return speed, len(set(tiles))

# Find the start and the end of the route
def find_start_end(grid):
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == "E":
                end = (i,j)
            elif char == "S":
                start = (i,j)
    return start, end

# Gets a list of lists representing the grid
with open("input16.txt") as f:
    grid = []
    for line in f.readlines():
        grid.append(list(line.strip()))

start, end = find_start_end(grid)

p1_answer, p2_answer = pathfind(grid, start)

print(f"The answer to part 1 is {p1_answer}")
print(f"The answer to part 2 is {p2_answer}")
