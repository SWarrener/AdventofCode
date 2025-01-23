# https://adventofcode.com/2024/day/18
import heapq

# Check if the coordinates are in bounds for the grid
def inbounds(x, y):
    if 0 <= y < size and 0 <= x < size:
        return True
    return False

# Create the grid from the list of coords
def create_grid(coords):
    return {(x, y): "#" if (x,y) in coords else "." for x,y in
        [(x,y) for x in range(size) for y in range(size)]}

# pathfind through the grid and find the shortest path to the end, if there are no paths
# return False
def pathfind(grid: dict, finish, start = (0,0)):
    open_list = [(0, *start)]
    closed_list = set()
    while True:
        if len(open_list) == 0:
            return False
        length, x, y = heapq.heappop(open_list)
        if (x,y) in closed_list:
            continue
        if (x,y) == finish:
            return length
        closed_list.add((x, y))
        for dx, dy in ((0,-1), (0,1), (1,0), (-1,0)):
            cx, cy = x+dx, y+dy
            if inbounds(cx, cy) and grid[cx, cy] == ".":
                heapq.heappush(open_list, (length+1, cx, cy))

# Add the coords one at a time until we find a blockage, then return those coordinates
def find_blockage(coords):
    grid = create_grid(coords[:1024])
    for i in range(1025, len(coords)):
        grid[coords[i]] = "#"
        if not pathfind(grid, (size-1, size-1)):
            return coords[i]
    return True

# extracts a list of tuples representing the coordinates
with open("input18.txt") as f:
    coords = []
    for line in f.readlines():
        coords.append(tuple(map(int, line.strip().split(","))))

size = max(x[0] for x in coords) + 1

p1_answer = pathfind(create_grid(coords[:1024]), (size-1, size-1))
print(f"The answer to part 1 is {p1_answer}")
p2_answer = find_blockage(coords)
print(f"The answer to part 2 is {p2_answer}")
