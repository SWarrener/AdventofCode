# https://adventofcode.com/2024/day/4

# Count the number of XMASes in the grid, look for SMAX so we don't have to bother rearranging
def count_xmas(grid, total):
    for x in grid:
        total += x.count("XMAS")
        total += x.count("SAMX")
    return total

# Rearrange the grid according to the function, and turn it back into strings
def manipulate_grid(grid, func):
    ngrid = [list(x) for x in grid]
    ngrid = func(ngrid)
    ngrid = ["".join(x) for x in ngrid]
    return ngrid

# Take the grid, look for XMAS then rearrange so whichever line we are looking down becomes strings for easy searching
# search for XMAS and then continue on
def solve_p1(grid):
    functions = [
        lambda l: l, # Horizontal lines
        lambda l: [[l[i+j][i] for i in range(len(l)) if i+j < len(l)] for j in range(len(l))], # Next 4 Diagonal lines
        lambda l: [[l[i][i+j] for i in range(len(l)) if i+j < len(l)] for j in range(1,len(l))], # First 2 TL -> BR
        lambda l: [[l[i][len(l)-1-j-i] for i in range(len(l)) if len(l)-1-j-i >= 0]
                   for j in range(len(l))], # then next 2 TR -> BL
        lambda l: [[l[i+j][len(l)-i-1] for i in range(len(l)) if len(l)-1-j >= 0 and i+j < len(l)]
                   for j in range(1,len(l))],
        lambda l: [[l[i][j] for i in range(len(l))] for j in range(len(l[0]))] # Vertical lines
    ]
    total = 0
    for func in functions:
        total = count_xmas(manipulate_grid(grid, func), total)
    return total

# Look for every A in the grid not on the edge, if it has 2 "M"s and 2 "S"s in the correct places
# and they are not diagonally across the A from each other it is a valid formation so add one to the total.
def solve_p2(grid):
    total = 0
    grid = [list(x) for x in grid]
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "A" and 0 < y < len(grid)-1 and 0 < x < len(grid[1])-1:
                to_check = (grid[y-1][x-1], grid[y-1][x+1], grid[y+1][x-1], grid[y+1][x+1])
                if to_check.count("M") == 2 and to_check.count("S") == 2:
                    tl,_,_,br = to_check
                    if tl != br:
                        total += 1
    return total

with open("input4.txt") as f:
    grid = []
    for line in f.readlines():
        grid.append(line.strip())

p1answer = solve_p1(grid)
p2answer = solve_p2(grid)

print(f"The answer to Part 1 is: {p1answer}")
print(f"The answer to Part 2 is: {p2answer}")
