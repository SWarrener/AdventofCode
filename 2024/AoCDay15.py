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
def move_robot(moves, grid):
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

# Calculate the score for the grid
def calc_score(grid):
    score = 0
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "O":
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

grid = move_robot(moves, grid)

p1_answer = calc_score(grid)
print(f"The answer to part 1 is {p1_answer}")
p2_answer = 2
print(f"The answer to part 2 is {p2_answer}")
