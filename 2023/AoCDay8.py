from math import lcm

def findname(name):
    for node in nodes:
        if node["name"] == name:
            return node

def checkfinished(locations):
    count = 0
    for location in locations:
        if location[0].endswith("Z") and location[1] == 0:
            location[1] = steps
        if location[1] != 0:
            count += 1
    if count == len(locations):
        return True
    else:
        return False
        
with open("input8.txt") as f:
    instructions = []
    nodes = []
    for i, line in enumerate(f.readlines()):
        if i == 0:
            instructions = list(line.strip())
        else:
            nodes.append({"name": line[:line.find("=")].strip(), "LR": line[line.find("(")+1:line.find(")")].split(", ")})

location = "AAA"
steps = 0

while location != "ZZZ":
    command = instructions[steps % len(instructions)]
    if command == "L":
        location = findname(location)["LR"][0]
    elif command == "R":
        location = findname(location)["LR"][1]
    steps += 1

print(f"The answer to part 1 is: {steps}")

steps = 0
locations = [[node["name"], 0] for node in nodes if node["name"].endswith("A")]

while not checkfinished(locations):
    command = instructions[steps % len(instructions)]
    templocations = []
    for location in locations:
        if command == "L":
            templocations.append([findname(location[0])["LR"][0], location[1]]) 
        elif command == "R":
            templocations.append([findname(location[0])["LR"][1], location[1]])
    locations = templocations
    steps += 1

p2answer = lcm(locations[0][1], locations[1][1], locations[2][1], locations[3][1], locations[4][1], locations[5][1])

print(f"The answer to part 2 is: {p2answer}")