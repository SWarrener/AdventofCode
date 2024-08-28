import numpy as np

# Basic pathfinding, starting from the middle and moving out, adding visited points to the
# close list. Use modulus to simulate the infinite copies of the grid. Also use a modulus check
# to ensure that we only consider tiles that can be reached in an even or odd number of moves
def pathfind(grid, start, step_count):
    reachable_plots = set()
    open_list = [(0, *start)]
    closed_list = set()
    while open_list:
        length, cur_x, cur_y = open_list.pop(0)
        if (cur_x, cur_y) in closed_list: continue
        elif length == step_count:
            reachable_plots.add((cur_x, cur_y))
            continue
        if length % 2 == step_count % 2: reachable_plots.add((cur_x, cur_y))
        closed_list.add((cur_x, cur_y))
        for dir_x, dir_y in {(1,0),(0,1),(-1,0),(0,-1)}:
            temp_x = dir_x+cur_x
            temp_y = dir_y+cur_y 
            if grid[temp_y % len(grid)][temp_x % len(grid)] != "#":
                open_list.append((length+1, temp_x, temp_y))
    return len(reachable_plots)

# Fit a quadratic polynomial (degree=2) through the points and
# evaluate the quadratic equation at the given x value
def interpolate_quadratic_equation(points, x):
    coef = np.polyfit(*zip(*points), 2)   
    return round(np.polyval(coef, x)) + 1 # The +1 deals with roudning down when we should be 
                                          # rounding up for my input. May be unecessary for others
with open("input21.txt") as f:
    grid = []
    for i, line in enumerate(f.readlines()):
        grid.append(list(line.strip()))
        if "S" in line:
            start = (i, line.find("S"))

p1answer = pathfind(grid, start, 64)

print(f"The answer to part 1 is: {p1answer}")

# As the column and row of the starting grid are empty the number of spaces you can reach after 
# n steps will be a quadratic, and can be interpolated quickly by finding the number of spaces
# reachable in 65, 65+131, and 65+131+131 steps.

points = [(i, pathfind(grid, start, 65 + (i * len(grid)))) for i in range(3)]
p2answer = interpolate_quadratic_equation(points, int(26501365/len(grid)))

print(f"The asnwer to part 2 is: {p2answer}")
