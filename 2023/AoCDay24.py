# https://adventofcode.com/2023/day/24

# Use the position and velocity data to calculate the y=mx+c form of the line the hailstone is taking
def create_line_data(hailstone):
    posx, posy, _ = hailstone["pos"]
    velx, vely, _ = hailstone["vel"]
    slope = vely/velx
    intercept = posy - (slope*posx)
    return (slope, intercept)

# Calculate where the two lines meet, returning those coords, or none if they do not meet
def line_intercept(a_slope, a_inter, b_slope, b_inter):
    if b_slope-a_slope == 0: #  The two lines are parallel
        return None
    x = -((b_inter-a_inter)/(b_slope-a_slope))
    y = a_slope*x + a_inter
    return (x, y)

# Check if the intercept is going forward from the current location of both hailstones.
# Check that the x and y differences between crossing point and start
# and the x and y in the velocity match signs. If they do it is in the future
def intercept_time(coords, pos1, pos2, vel1, vel2):
    cross_x, cross_y = coords
    ax, ay, _, bx, by, _ = *pos1, *pos2
    avx, avy, _, bvx, bvy, _ = *vel1, *vel2
    if (cross_y-ay) * avy > 0 and (cross_x-ax) * avx > 0 and (cross_y-by) * bvy > 0 and (cross_x-bx) * bvx > 0:
        return True
    return False

# Go through the hailstones and compare their paths. If they are in bounds and all other checks
# are good then add the crossing point to the total.
def solve_p1(hailstones):
    total = 0
    for i, stone_1 in enumerate(hailstones):
        for stone_2 in hailstones[i:]:
            if stone_1 != stone_2:
                cross = line_intercept(*stone_1["p1_data"], *stone_2["p1_data"])
                if cross and intercept_time(cross, stone_1["pos"], stone_2["pos"], stone_1["vel"], stone_2["vel"]):
                    if p1_min_xy_pos <= cross[0] <= p1_max_xy_pos and p1_min_xy_pos <= cross[1] <= p1_max_xy_pos:
                        total += 1
    return total

# Extract a list of dictionaries, where each dictionary contains a tuple of the start pos
# and the velocity for each hailstone.
with open("input24.txt") as f:
    hailstones = []
    for line in f.readlines():
        position = tuple(map(int, line[:line.find("@")].strip().split(", ")))
        velocity = tuple(map(int, line[line.find("@")+1:].strip().split(", ")))
        hailstones.append({"pos": position, "vel": velocity})

p1_min_xy_pos = 200000000000000
p1_max_xy_pos = 400000000000000

for stone in hailstones:
    stone["p1_data"] = create_line_data(stone)

p1_answer = solve_p1(hailstones)
print(f"The answer to part 1 is: {p1_answer}")
