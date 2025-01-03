# https://adventofcode.com/2024/day/14
from math import prod

# Simulates a robot moving for 100 seconds
def move_robot(robot):
    x, y = robot["pos"]
    dx, dy = robot["vel"]
    robot["new_pos"] = ((x + dx*100) % BOUNDS[0], (y+dy*100) % BOUNDS[1])
    return robot

# Calculates the score based on the robot's final position
def calculate_score(robots):
    scores = [0,0,0,0]
    hx, hy = (BOUNDS[0]-1)/2, (BOUNDS[1]-1)/2
    for robot in robots:
        x, y = robot["new_pos"]
        if x > hx and y > hy:
            scores[0] += 1
        elif x < hx and y > hy:
            scores[1] += 1
        elif x > hx and y < hy:
            scores[2] += 1
        elif x < hx and y < hy:
            scores[3] += 1
    return scores

# writes to a file the grid with the positions of all the robots
def print_grid(counter, robots):
    positions = {robot["pos"] for robot in robots}
    with open("14answer.txt", "a+") as f:
        f.write(f"\n\n{counter}\n")
    for y in range(BOUNDS[1]):
        line = ""
        for x in range(BOUNDS[0]):
            if (x,y) in positions:
                line += "X"
            else:
                line += "."
        with open("14answer.txt", "a+") as f:
            f.write(line+"\n")

# Moves robots
def find_christmas(robots):
    for i in range(500):
        print_grid(i, robots)
        for robot in robots:
            x, y = robot["pos"]
            dx, dy = robot["vel"]
            robot["pos"] = ((x + dx) % BOUNDS[0], (y+dy) % BOUNDS[1])


# Gets a list of dicts representing each robot
with open("input14.txt") as f:
    robots = []
    for line in f.readlines():
        pos, vel = line.strip().split(" ")
        position = (int(pos[pos.find("=")+1:pos.find(",")]), int(pos[pos.find(",")+1:]))
        velocity = (int(vel[vel.find("=")+1:vel.find(",")]), int(vel[vel.find(",")+1:]))
        robots.append({"pos": position, "vel": velocity})

BOUNDS = (101,103) # 101, 103 for full 11, 7 for test. Needs to be manually entered

for robot in robots:
    robot = move_robot(robot)

p1_answer = prod(calculate_score(robots))
print(f"The answer to part 1 is {p1_answer}")

# Use the generated file and manually search through to find the first horizontal and vertical lines in the grid
# Replace the 143 and 99 respectively with the first grids in which you see those patterns
find_christmas(robots)

p2_answer = 0

xvals = [99+101*x for x in range(0,104)]
yvals = [143+103*y for y in range(0,102)]
for val in yvals:
    if val in xvals:
        p2_answer = val

print(f"The answer to part 2 is {p2_answer}")
