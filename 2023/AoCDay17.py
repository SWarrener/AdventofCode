import heapq

def InBounds(grid, coords):
    if coords[0] < len(grid) and coords[1] < len(grid) and coords[0] >= 0 and coords[1] >= 0:
        return True
    return False

def Pathfind(grid, start, end, move_high, move_low):
    open_list = [(0, *start, 0,0)]
    closed_list = set()
    while open_list:
        # Always pops the lowest heat_loss value, so will produce the best path so far to be worked on
        heat_loss, cur_x, cur_y, prev_x, prev_y = heapq.heappop(open_list)
        if (cur_x, cur_y) == end: return heat_loss
        if (cur_x, cur_y, prev_x, prev_y) in closed_list: continue
        closed_list.add((cur_x, cur_y, prev_x, prev_y))
        for dir_x, dir_y in {(1,0),(0,1),(-1,0),(0,-1)}-{(prev_x,prev_y),(-prev_x,-prev_y)}:
            temp_x, temp_y, temp_heat = cur_x, cur_y, heat_loss
            # We need to move through the tiles so we iterate through them even if they aren't
            # eligible turning places
            for i in range(1, move_high+1):
                temp_x = temp_x+dir_x
                temp_y = temp_y+dir_y
                if InBounds(grid, (temp_x, temp_y)):
                    temp_heat += grid[temp_y][temp_x]
                    if i >= move_low: # Check to ensure the turn is valid for part 2
                        heapq.heappush(open_list, (temp_heat, temp_x, temp_y, dir_x, dir_y))

with open("input17.txt") as f:
    grid = []
    for line in f.readlines():
        grid.append(list(map(int, list(line.strip()))))

p1answer = Pathfind(grid, (0,0), (len(grid)-1, len(grid[0])-1), 3, 1)
p2answer = Pathfind(grid, (0,0), (len(grid)-1, len(grid[0])-1), 10, 4)

print(f"The answer to part 1 is {p1answer}")
print(f"The answer to part 2 is {p2answer}")