# https://adventofcode.com/2023/day/8
from math import lcm

# Check if all of the paths in part two have found their way to a destination location.
# If they have we have finished and can run the LCM
def checkfinished(locations, steps):
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


# Go through the list until you find the ZZZ node, counting how many steps it takes, and return that
def solve_p1(instructions, nodes):
    location = "AAA"
    steps = 0
    while location != "ZZZ":
        command = instructions[steps % len(instructions)]
        if command == "L":
            location = nodes[location]["LR"][0]
        elif command == "R":
            location = nodes[location]["LR"][1]
        steps += 1
    return steps


# Go through the list simultaneously for all start positions. Once we have step counts for all of
# them to finish, use LCM to work out when they will all finish on the same step. 
def solve_p2(instructions, nodes):
    steps = 0
    locations = [[node["name"], 0] for node in nodes.values() if node["name"].endswith("A")]

    while not checkfinished(locations, steps):
        command = instructions[steps % len(instructions)]
        templocations = []
        for location in locations:
            if command == "L":
                templocations.append([nodes[location[0]]["LR"][0], location[1]]) 
            elif command == "R":
                templocations.append([nodes[location[0]]["LR"][1], location[1]])
        locations = templocations
        steps += 1

    return lcm(*[location[1] for location in locations])


# Extract two lists, one is the list of instructions and the other is a list of
# dictionaries representing each node, with its name and a two item list of its
# left and right target locations. 
with open("input8.txt") as f:
    instructions = []
    nodes = {}
    for i, line in enumerate(f.readlines()):
        if line == "\n": continue
        if i == 0:
            instructions = list(line.strip())
        else:
            name = line[:line.find("=")].strip()
            nodes[name] = {"name": name, "LR": line[line.find("(")+1:line.find(")")].split(", ")}

p1_answer = solve_p1(instructions, nodes)

print(f"The answer to part 1 is: {p1_answer}")

p2answer = solve_p2(instructions, nodes)

print(f"The answer to part 2 is: {p2answer}")