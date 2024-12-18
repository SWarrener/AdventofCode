# https://adventofcode.com/2024/day/8
import itertools

# Checks if coordinates are in bounds of the grid
def inbounds(grid, coords):
    if 0 <= coords[0] < len(grid) and 0 <= coords[1] < len(grid[0]):
        return True
    return False

# Find the coords of all antenna and returns them as a dict with the signal
# as the key and a list of coords as the value
def find_antenna(grid):
    antenna = {}
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char != ".":
                if char not in antenna:
                    antenna[char] = [(y,x)]
                else:
                    antenna[char].append((y,x))
    return antenna

# Finds the antinodes by calculating the slope of the line between each antenna pair and
# finding the coords at the distances relevant to the part
def find_antinodes(grid: list, antenna: dict, p2 = False):
    antinodes = set()
    for coords in antenna.values():
        for a, b in itertools.combinations(coords, 2):
            ay, ax, by, bx = *a, *b
            dy, dx = (ay - by, ax - bx)
            for pos in ((ay+dy,ax+dx),(by-dy,bx-dx)):
                if inbounds(grid, pos):
                    antinodes.add(pos)
            if p2:
                while inbounds(grid, (ay := ay + dy, ax := ax + dx)):
                    antinodes.add((ay, ax))
                while inbounds(grid, (by := by - dy, bx := bx - dx)):
                    antinodes.add((by, bx))
        if p2 and len(coords) > 1:
            for coord in coords:
                antinodes.add(coord)

    return len(antinodes)

# Gets a list of lists representing the grid
with open("input8.txt") as f:
    grid = []
    for line in f.readlines():
        grid.append(list(line.strip()))

antenna = find_antenna(grid)

p1_answer = find_antinodes(grid, antenna)
print(f"The answer to part 1 is {p1_answer}")
p2_answer = find_antinodes(grid, antenna, True)
print(f"The answer to part 2 is {p2_answer}")
