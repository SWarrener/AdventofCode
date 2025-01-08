# https://adventofcode.com/2024/day/15

# Finds the position of the robot and returns it, removing it from the grid
def find_robot(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "@":
                grid[y][x] = "."
                return y,x
    return None

# Move the robot through the grid, pushing the boxes until we run out of moves
def move_robot_p1(moves, grid):
    ry, rx = find_robot(grid)
    dirs = {">": (0,1), "<": (0,-1), "^": (-1,0), "v": (1,0)}
    for move in moves:
        dy, dx = dirs[move]
        boxes = []
        cy, cx = ry, rx
        while True:
            cy, cx = cy+dy, cx+dx
            char = grid[cy][cx]
            if char == "#":
                break
            if char == "O":
                boxes.append((cy,cx))
            if char == ".":
                for by, bx in boxes:
                    grid[by][bx] = "."
                for by, bx in ((by+dy,bx+dx) for by,bx in boxes):
                    grid[by][bx] = "O"
                ry, rx = ry+dy,rx+dx
                break
    return grid

# Turns the p1 grid into the part 2 grid
def create_p2_grid(grid):
    charmap = {"#": ["#","#"], "O": ["[","]"], ".": [".","."], "@": ["@","."]}
    new = []
    for line in grid:
        newl = []
        for char in line:
            newl += charmap[char]
        new.append(newl)
    return new

# Deals with vertical moves for part 2. If the robot moves into a box, keeping looking
# in the direction of travel until we find out if the box can or can't be moved. Only then
# actually move the box
def check_vertical(ry, rx, dy, grid):
    old_boxes = {}
    box_map = {"]": (-1,"["), "[": (1,"]")}
    cy, cx = ry+dy, rx
    char = grid[cy][cx]
    if char == "#":
        return ry, rx
    if char == ".":
        return cy, cx
    old_boxes[cy,cx] = char
    bx, bc = box_map[char]
    old_boxes[cy,cx+bx] = bc
    frontier = {(y+dy,x): grid[y+dy][x] for y,x in old_boxes}
    while True:
        if "#" in frontier.values():
            return ry, rx
        if all(x == "." for x in frontier.values()):
            break
        frontier = dict(sorted(frontier.items(), key=lambda i: i[0][1]))
        frontier_list = list(frontier)
        y, x = frontier_list[0]
        if grid[y][x] == "]":
            frontier[y,x-1] = "["
        y, x = frontier_list[-1]
        if grid[y][x] == "[":
            frontier[y,x+1] = "]"
        new_frontier = {}
        for coords, char in frontier.items():
            y, x = coords
            if char in box_map:
                old_boxes[y,x] = char
                new_frontier[y+dy,x] = grid[y+dy][x]
        frontier = new_frontier
    new_boxes = {(k[0]+dy,k[1]): v for k,v in old_boxes.items()}
    for y, x in old_boxes:
        grid[y][x] = "."
    for coords, char in new_boxes.items():
        y, x = coords
        grid[y][x] = char
    return cy, cx

# Deals with any horizontal moves for part 2, similar idea to part 1 except
# an extra step to keep the boxes paired together
def check_horizontal(ry, rx, dx, grid):
    old_boxes = {}
    cy, cx = ry, rx
    while True:
        cx = cx+dx
        if (cy,cx) in old_boxes:
            continue
        char = grid[cy][cx]
        if char == "#":
            return ry,rx
        if char in ("[","]"):
            old_boxes[cy,cx] = char
            if char == "[":
                old_boxes[cy,cx+1] = "]"
            elif char == "]":
                old_boxes[cy,cx-1] = "["
        if char == ".":
            new_boxes = {(k[0],k[1]+dx): v for k,v in old_boxes.items()}
            for y, x in old_boxes:
                grid[y][x] = "."
            for coords, char in new_boxes.items():
                y, x = coords
                grid[y][x] = char
            return ry,rx+dx

# Move the robot around for part 2
def move_robot_p2(moves, grid):
    ry, rx = find_robot(grid)
    dirs = {">": (0,1), "<": (0,-1), "^": (-1,0), "v": (1,0)}
    for move in moves:
        dy, dx = dirs[move]
        if dy == 0:
            ry, rx = check_horizontal(ry, rx, dx, grid)
        else:
            ry, rx = check_vertical(ry, rx, dy, grid)
    return grid


# Calculate the score for the grid
def calc_score(grid, target):
    score = 0
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == target:
                score += 100*y + x
    return score

# Extracts a string with the list of moves and a list of lists representing the grid
with open("input15.txt") as f:
    grid = []
    moves = ""
    for line in f.readlines():
        if line.startswith("#"):
            grid.append(list(line.strip()))
        else:
            moves += line.strip()

p2_grid = create_p2_grid(grid)

grid = move_robot_p1(moves, grid)
p1_answer = calc_score(grid, "O")
print(f"The answer to part 1 is {p1_answer}")

p2_grid = move_robot_p2(moves, p2_grid)
p2_answer = calc_score(p2_grid, "[")
print(f"The answer to part 2 is {p2_answer}")
