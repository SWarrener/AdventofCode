from shapely.geometry import Polygon

def CreateCoordinates(instructions):
    coords = [(0,0)]
    for instruction in instructions:
        current = coords[-1]
        if instruction[0] == "U" or instruction[0] == '3':
            coords.append((current[0], current[1] + instruction[1]))
        elif instruction[0] == "D" or instruction[0] == '1':
            coords.append((current[0], current[1] - instruction[1]))
        elif instruction[0] == "R" or instruction[0] == '0':
            coords.append((current[0] + instruction[1], current[1]))
        elif instruction[0] == "L" or instruction[0] == '2':
            coords.append((current[0] - instruction[1], current[1]))
    return coords

def ComputeArea(coords):
    pgon = Polygon(coords)
    # We aren't looking for the area, but number of points including the boundaries.
    # So we need to use this formula instead of simply using the boundaries
    return int(pgon.area + pgon.length/2 + 1)

with open("input18.txt") as f:
    instructions = []
    for line in f.readlines():
        instructions.append((line[0], 
                             int(line[line.find(" "):line.rfind(" ")]),
                             line.strip()[line.find("(")+1:-1]))

# Take the first two values from the input line
p1coords = CreateCoordinates([(x[0],x[1]) for x in instructions])
p1answer = ComputeArea(p1coords)

# Take the last digit of the hex code as the instruction and
# the first 5 digits after the hash of the hex code for the distance
p2coords = CreateCoordinates([(x[2][-1], int(x[2][1:-1],16)) for x in instructions])
p2answer = ComputeArea(p2coords)

print(f"The answer to part 1 is {p1answer}.")
print(f"The answer to part 2 is {p2answer}.")
