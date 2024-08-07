def isvalid(x, y):
    if x < 0 or x >= 140 or y < 0 or y>=140:
        return False
    elif grid[x][y].isdigit() or grid[x][y] == ".":
        return False
    else:
        return True
    
def isneighbour(star, set):
    Starx = [star[0], star[0]+1, star[0]-1]
    Stary = [star[1], star[1]+1, star[1]-1]
    if set[0] in Starx and set[1] in Stary or set[0] in Starx and set[2]-1 in Stary:
        return True
    else:
        return False
    
with open("input3.txt") as f: #part 1
    total = 0
    grid = []
    numbers = []
    stars = []
    for i, line in enumerate(f.readlines()):
        grid.append(list(line))
        numend = 0
        for j, char in enumerate(line):
            if j < numend:
                continue
            if char.isdigit():
                for x, char2 in enumerate(line[j:]):
                    if not char2.isdigit():
                        numend = x + j
                        break
                numbers.append([i, j, numend, line[j:numend]])
            if char == '*':
                stars.append([i, j])
    for set in numbers:
        x = set[0]
        y1 = set[1]
        y2 = set[2]
        if isvalid(x, y1-1) or isvalid(x-1, y1-1) or isvalid(x+1, y1-1) or isvalid(x+1, y1) or isvalid(x-1, y1) or isvalid(x, y2) or isvalid(x+1, y2) or isvalid(x-1, y2) or isvalid(x-1, y2-1) or isvalid(x-1, y2-2) or isvalid(x+1, y2-1) or isvalid(x+1, y2-2):
            total+= int(set[3])
    print(f"The answer to part 1 is: {total}")

    p2total = 0

    for star in stars:
        neighbours = 0
        cachedtotal = 1
        for set in numbers:
            if isneighbour(star, set):
                neighbours += 1
                cachedtotal *= int(set[3])
        if neighbours >= 2:
            p2total += cachedtotal
    print(f"The answer to part 2 is: {p2total}")