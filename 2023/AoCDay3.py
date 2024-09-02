# https://adventofcode.com/2023/day/3
import re

# Check if the coordinates are any symbol, if they are return true. 
def isvalid(x, y):
    if  x < 0 or x >= len(grid) or y < 0 or y >= len(grid):
        return False
    if grid[x][y].isdigit() or grid[x][y] == ".":
        return False
    else:
        return True

# Check if a star neighbours a number.
def isneighbour(star, set):
    Starx = [star[0], star[0]+1, star[0]-1]
    Stary = [star[1], star[1]+1, star[1]-1]
    if set[0] in Starx and set[1] in Stary or set[0] in Starx and set[2] in Stary:
        return True
    else:
        return False
    
# Extract the grid, a list of star coordinates, and a data about each number
# The number data is its x value, the y value of its start and end, and the number itself.
with open("input3.txt") as f:
    grid, numbers, stars = [], [], []
    for i, line in enumerate(f.readlines()):
        grid.append(list(line))
        numend = 0
        for j, char in enumerate(line):
            if j < numend:
                continue
            if char.isdigit():
                numend = re.search("[^0-9]", line[j:]).start() + j
                numbers.append((i, j, numend-1, int(line[j:numend])))
            if char == '*':
                stars.append([i, j])

# For each number check all their surroundings, if we find a symbol break and add to the total.
p1_answer = 0
for set in numbers:
    x, y1, y2, num = set
    for dx, dy in {(0, -1), (-1, -1), (1, -1), (1, 0), (-1, 0), (0, 1), (1, 1), (-1, 1)}:
        if isvalid(x+dx, y1+dy) or isvalid(x+dx, y2+dy):
            p1_answer += num
            break
print(f"The answer to part 1 is: {p1_answer}")

# For each star check if it has 2 number neighbours, if it does times the numbers together
# and add that to the total. 
p2_answer = 0
for star in stars:
    neighbours, cachedtotal = 0, 1
    for set in numbers:
        if isneighbour(star, set):
            neighbours += 1
            cachedtotal *= set[3]
    if neighbours == 2:
        p2_answer += cachedtotal
print(f"The answer to part 2 is: {p2_answer}")
