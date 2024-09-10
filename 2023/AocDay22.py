# https://adventofcode.com/2023/day/22

# Take the start and end point of a brick and generate the rest of the coords based on that
def fill_bricks(bricks):
    for brick in bricks.values():
        start, end = brick["start"], brick["end"]
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                for z in range(start[2], end[2]+1):
                    brick["coords"].append((x, y, z))


# Put the bricks and ground into the grid
def fill_grid(grid, bricks):
    for brick in bricks.values():
        for coords in brick["coords"]:
            x, y, z = coords
            grid[x][y][z] = 1
    for x in range(len(grid)):  #  Fill the bottom of the grid, aka the ground
        for y in range(len(grid[x])):
            grid[x][y][0] = 1


# Sort the bricks by lowest z value, lowest first. Then for each x, y value that brick operates find the
# next occupied tile below that. The highest of these is where the brick will sit. Move the brick to that
# position in the grid. Update the brick coords to its new position. 
def drop_bricks(grid, bricks):
    bricks = dict(sorted(bricks.items(), key=lambda item: min(coord[2] for coord in item[1]["coords"])))
    for k, brick in bricks.items():
        coords = brick["coords"]
        new_coords = []
        if brick["end"][2] - brick["start"][2] == 0:
            resting_z = max([(z - grid[x][y][:z][::-1].index(1)) for x, y, z in coords])
            for x, y, z in coords:
                grid[x][y][z] = 0
                grid[x][y][resting_z] = 1
                new_coords.append((x,y,resting_z))
        else:
            x, y, z = brick["start"]
            resting_z = z - grid[x][y][:z][::-1].index(1)
            for i in range(len(coords)):
                grid[x][y][z+i] = 0
                grid[x][y][resting_z+i] = 1
                new_coords.append((x,y,resting_z+i))
        brick["coords"] = new_coords


# Find which brick fills a coordinate, also use the calling brick to populate supported_by field
def find_brick_by_coords(coords, bricks, supported_key):
    for k, brick in bricks.items():
        if coords in brick["coords"]:
            if supported_key not in brick["supported_by"]:
                brick["supported_by"].append(supported_key)
            return k


# Find which bricks support other bricks by checking tiles directly above, use the information to
# populate the supports field as well. 
def find_support(grid, bricks):
    for k, brick in bricks.items():
        coords = brick["coords"]
        for x, y, z in coords:
            check_z = z + 1
            if (x, y, check_z) in coords: continue
            if grid[x][y][check_z] == 1:
                supports_key = find_brick_by_coords((x, y, check_z), bricks, k)
                if supports_key not in brick["supports"]:
                    brick["supports"].append(supports_key)


# For each brick see if the bricks it supports are supported by anything else. If they
# are, or it supports no bricks, it can be safely disintegrated.
def try_disintegration(bricks):
    total = 0
    for k, brick in bricks.items():
        if len(brick["supports"]) == 0:
            total += 1
            continue
        else:
            eligible = True
            for key in brick["supports"]:
                if len(bricks[key]["supported_by"]) <= 1:
                    eligible = False
            if eligible: total += 1
    return total

# Generate a dictionary of bricks
with open("input22.txt") as f:
    bricks = {}
    for i, line in enumerate(f.readlines()):
        start, end = tuple(line.strip().split("~"))
        bricks[i] = {"start": tuple(map(int, start.split(","))), 
                     "end" : tuple(map(int, end.split(","))),
                     "coords": [],
                     "supports": [],
                     "supported_by": []}

fill_bricks(bricks)

# Find the maximum dimensions that the grid needs to be and create the grid
max_finder = lambda x, list_: max([max([point[x] for point in sub]) for sub in list_])
highest_coords = [max_finder(i, [bricks[k]["coords"] for k in bricks.keys()]) for i in range(3)]

grid = [[[0]*(highest_coords[2]+1) for _ in range(highest_coords[1]+1)] for _ in range(highest_coords[0]+1)]

fill_grid(grid, bricks)

drop_bricks(grid, bricks)

find_support(grid, bricks)

p1_answer = try_disintegration(bricks)
print(f"The answer to part 1 is: {p1_answer}")