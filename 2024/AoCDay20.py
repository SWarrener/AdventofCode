# https://adventofcode.com/2024/day/20

def find_start_end_length(grid):
    count = 0
    for k, v in grid.items():
        if v == "S":
            start = k
        elif v == "E":
            end = k
        elif v == ".":
            count += 1
    return start, end, count + 1

# Do some basic pathfinding and change the numbers in the grid to enable the part 1 solution
def pathfind(start, end, p1_grid):
    open_list = [(0, *start, False)]
    closed_list = set()
    while True:
        score, cx, cy, cheat = open_list.pop()
        if (cx, cy) == end:
            p1_grid[start] = 0
            return p1_grid
        closed_list.add((cx, cy))
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = cx + dx, cy + dy
            if p1_grid[nx, ny] == "#" or (nx, ny) in closed_list:
                continue
            p1_grid[nx, ny] = score + 1
            open_list.append((score+1, nx, ny, cheat))

# Find the 2 length cheats for the part 1 solution
def find_cheats(grid: dict, target):
    count = 0
    for k, v in grid.items():
        if v == "#":
            continue
        for dx, dy in ((2, 0), (-2, 0), (0, 2), (0, -2)):
            pos = tuple(a-b for a,b in zip(k, (dx, dy)))
            if pos in grid.keys() and grid[pos] != "#":
                if grid[tuple((a+b)/2 for a,b in zip(k, pos))] == "#" and grid[k] - grid[pos] + 2 <= -target:
                    count += 1
    return count

# Any two tiles with a manhattan distance of <= 20 and a diff + manhattan of <= -100 would count for the
# cheat. This would work for p1 as well but is a lot slower than the above solution
def solve_p2(grid: dict, target, distance):
    count = 0
    for k, v in grid.items():
        cx, cy = k
        if v == "#":
            continue
        for k2, v2 in grid.items():
            if v2 == "#":
                continue
            nx, ny = k2
            man_distance = abs(cx-nx) + abs(cy-ny)
            if man_distance <= distance:
                if grid[k] - grid[k2] + man_distance <= -target:
                    count += 1
    return count

# gets a dictionary representing the grid
with open("input20.txt") as f:
    grid = {(i,j): char for i, line in enumerate(f.readlines()) for j, char in enumerate(line.strip())}

start, end, base_length = find_start_end_length(grid)

num_grid = pathfind(start, end, grid.copy())

p1_answer = find_cheats(num_grid, 100)
print(f"The answer to part 1 is {p1_answer}")
p2_answer = solve_p2(num_grid, 100, 20)
print(f"The answer to part 2 is {p2_answer}")
