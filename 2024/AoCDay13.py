# https://adventofcode.com/2024/day/13

# Calculate the number of moves taken to get to the prize locations using some linear algebra
def count_tokens(machines, p1 = True):
    for machine in machines:
        px, py = machine["prize"]
        ax, ay = machine["A"]
        bx, by = machine["B"]
        if p1 and (ax*100 + bx*100 < px or ay*100 + by*100 < py):
            yield 0
        else:
            a = abs((by*px - bx*py)/(ay*bx - ax*by))
            b = abs((px-ax*a)/bx)
            if int(a) != a or int(b) != b: # check for non-integer solutions (which are invalid)
                continue
            yield round(a)*3 + round(b)

# Extracts the list of machines, with each machine being represented by a dictionary containing
# its prize coords and the moves for the two buttons
with open("input13.txt") as f:
    machines = []
    for line in f.readlines():
        data = line.strip()
        if "A" in data:
            a = (int(line[line.find("+")+1:line.find(",")]), int(line[line.rfind("+")+1:]))
        elif "B" in data:
            b = (int(line[line.find("+")+1:line.find(",")]), int(line[line.rfind("+")+1:]))
        elif "P" in data:
            prize = (int(line[line.find("=")+1:line.find(",")]), int(line[line.rfind("=")+1:]))
            machines.append({"prize": prize, "A": a, "B": b})

p1_answer = sum(count_tokens(machines))
print(f"The answer to part 1 is {p1_answer}")

for machine in machines:
    x,y = machine["prize"]
    machine["prize"] = (10000000000000+x,10000000000000+y)

p2_answer = sum(count_tokens(machines, False))
print(f"The answer to part 2 is {p2_answer}")
