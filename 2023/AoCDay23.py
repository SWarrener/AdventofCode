# https://adventofcode.com/2023/day/23

# Check if coordinates are inside the grid, return True if that is the case
def inbounds(grid, x, y):
    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        return True
    return False

# Check that we are going the correct direction for any of the slopes, if we are return True
def try_special_character(char, direction):
    if char == ">" and direction == (0, 1):
        return True
    if char == "<" and direction == (0, -1):
        return True
    if char == "^" and direction == (-1, 0):
        return True
    if char == "v" and direction == (1, 0):
        return True
    return False

# Pathfind through the grid, returning the length of all paths to the end.

def pathfind(grid, start, end):
    open_list = [(0, *start, set())]
    lengths = []
    while open_list:
        cur_length, cur_y, cur_x, closed_list = open_list.pop(0)
        if (cur_y, cur_x) in closed_list:
            continue
        if (cur_y, cur_x) == end:
            lengths.append(cur_length)
            continue
        closed_list.add((cur_y, cur_x))
        for diff_y, diff_x in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            temp_y, temp_x = cur_y+diff_y, cur_x+diff_x
            if (temp_y, temp_x) in closed_list or not inbounds(grid, temp_x, temp_y):
                continue
            char = grid[temp_y][temp_x]
            if char == '#':
                continue
            if char == '.':
                open_list.append((cur_length+1, temp_y, temp_x, closed_list.copy()))
            else:
                if try_special_character(char, (diff_y, diff_x)):
                    open_list.append((cur_length+1, temp_y, temp_x, closed_list.copy()))
                else:
                    continue
    return lengths

with open("input23.txt") as f:
    grid = []
    for line in f.readlines():
        grid.append(list(line.strip()))

start = (0, grid[0].index("."))
end = (len(grid)-1, grid[-1].index("."))

p1answer = max(pathfind(grid, start, end))

print(f"The answer to part 1 is {p1answer}")
