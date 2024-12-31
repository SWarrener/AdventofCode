# https://adventofcode.com/2024/day/12

# Check if coordinates are in bounds or not
def inbounds(y, x):
    if 0 <= y <= max_y and 0 <= x <= max_x:
        return True
    return False

# Iterate through the grid, for each new region start a flood fill to find its area and pathfind
# marking any tile that we pass through. Return the regions.
def find_regions(grid: dict):
    regions = []
    for coords, tile in grid.items():
        if tile["fenced"]:
            continue
        area, perimeter = 1,0
        grid[coords]["fenced"] = True
        char = tile["char"]
        paths, a_coords = [coords], {coords}
        while paths:
            y, x = paths.pop()
            for dy, dx in ((0,1), (1,0), (-1,0), (0,-1)):
                cy, cx = y + dy, x + dx
                if not inbounds(cy,cx):
                    perimeter += 1
                    continue
                if grid[cy,cx]["fenced"] is True and grid[cy,cx]["char"] == char:
                    continue
                if grid[cy,cx]["char"] == char:
                    area += 1
                    grid[cy,cx]["fenced"] = True
                    paths.append((cy,cx))
                    a_coords.add((cy,cx))
                else:
                    perimeter += 1
        regions.append({"area": area, "perimeter": perimeter, "a_coords": a_coords})
    return regions

# Maths tip: numbers of corners = number of sides. Find all the corners by checking the 8
# possibilities for each corner, adding to the total if there is a corner
def find_corners(regions):
    for region in regions:
        corners = 0
        a_coords = region["a_coords"]
        for y, x in a_coords:
            for dy, dx, dy2, dx2 in ((-1,0,0,-1),(1,0,0,-1),(-1,0,0,1),(1,0,0,1)):
                if (y+dy,x+dx) not in a_coords and (y+dy2,x+dx2) not in a_coords:
                    corners += 1
            for dy, dx, dy2, dx2, dy3, dx3 in ((-1,0,0,-1,-1,-1),(1,0,0,-1,1,-1),(-1,0,0,1,-1,1),(1,0,0,1,1,1)):
                if (y+dy,x+dx) in a_coords and (y+dy2,x+dx2) in a_coords and (y+dy3,x+dx3) not in a_coords:
                    corners += 1
        region["sides"] = corners
    return regions

# Represents the grid as a dictionary, where the key is the tile coords and the value is a dict
# containing the char and whether the tile has been visited or not.
with open("input12.txt") as f:
    grid = {}
    for y, line in enumerate(f.readlines()):
        for x, char in enumerate(line.strip()):
            grid[y,x] = {"char": char, "fenced": False}

max_y = max(y for y,_  in grid)
max_x = max(x for _,x in grid)

regions = find_regions(grid)
regions = find_corners(regions)

p1_answer = sum(x["area"]*x["perimeter"] for x in regions)
print(f"The answer to part 1 is {p1_answer}")
p2_answer = sum(x["area"]*x["sides"] for x in regions)
print(f"The answer to part 2 is {p2_answer}")
