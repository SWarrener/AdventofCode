from math import prod

# Go through each test in the calculation. If it is true, return the next step
# If not keep going until we hit the fallback.
def TestWorkflow(part, workflow):
    for calc in workflow:
        if calc.find(":") == -1:
            return calc
        if calc.find("<") != -1:
            if part[calc[0]] < int(calc[calc.find("<")+1:calc.find(":")]):
                return calc[calc.find(":")+1:]
        if calc.find(">") != -1:
            if part[calc[0]] > int(calc[calc.find(">")+1:calc.find(":")]):
                return calc[calc.find(":")+1:]
    return None

# Take each part and test its current workflow. If it is allowed, add it to the
# allowed list. If rejected do nothing with it. If it has a new workflow, then
# re-add it to the list with the new workflow
def ProcessParts(active_parts, workflows):
    allowed_parts = []
    while active_parts:
        flow, current_part = active_parts.pop(0)
        flow = TestWorkflow(current_part, workflows[flow])
        if flow == "A":
            allowed_parts.append(current_part)
        elif flow != "R":
            active_parts.append((flow, current_part))
    return allowed_parts

# Take each workflow and work out which values of each x, m, a, s lead to each outcome
# and return the bounds of values and the next workflow
def CalculateWorkflow(workflow, bounds):
    results = []
    for calc in workflow:
        temp_bounds = bounds.copy()
        if calc.find(":") == -1:
            results.append((calc, bounds))
        elif calc.find("<") != -1:
            cur_bound = calc[0] + "h"
            value = int(calc[calc.find("<")+1:calc.find(":")]) - 1
            if value < bounds[cur_bound]:
                temp_bounds[cur_bound] = value
            results.append((calc[calc.find(":")+1:], temp_bounds))
            cur_bound = calc[0] + "l"
            if value + 1 > bounds[cur_bound]:
                bounds[cur_bound] = value + 1
        elif calc.find(">") != -1:
            cur_bound = calc[0] + "l"
            value = int(calc[calc.find(">")+1:calc.find(":")]) + 1
            if value > bounds[cur_bound]:
                temp_bounds[cur_bound] = value
            results.append((calc[calc.find(":")+1:], temp_bounds))
            cur_bound = calc[0] + "h"
            if value - 1 < bounds[cur_bound]:
                bounds[cur_bound] = value - 1
    return results

# Work through each workflow, calculating which bounds of numbers lead to an accepted outcome.
# Once it has been accepted, add the bounds to a list which is returned once all workflows
# have been fully explored
def ProcessWorkflows(workflows):
    possibilities = [("in", {"xl":1,"xh":4000,"ml":1,"mh":4000,"al":1,"ah":4000,"sl":1,"sh":4000})]
    approved_possibilities = []
    while possibilities:
        flow, current_bounds = possibilities.pop(0)
        results = CalculateWorkflow(workflows[flow], current_bounds)
        for flow, bounds in results:
            if flow == "A":
                approved_possibilities.append(bounds)
            elif flow != "R":
                possibilities.append((flow, bounds))
    return approved_possibilities

with open("input19.txt") as f:
    workflows = {}
    parts = []
    for line in f.readlines():
        if line[0] == "{":
            temp = {item[0]: int(item[item.find("=")+1:]) for item in line.strip()[line.find("{")+1:-1].split(",")}
            # ('in', {'x': 787, 'm': 2655, 'a': 1222, 's': 2876})
            parts.append(("in", temp))
        elif line != "\n":
            # 'px': ['a<2006:qkq', 'm>2090:A', 'rfg']
            workflows[line[:line.find("{")]] = line.strip()[line.find("{")+1:-1].split(",")

allowed_parts = ProcessParts(parts, workflows)
allowed_bounds = ProcessWorkflows(workflows)

p1answer = sum(v for part in allowed_parts for v in part.values())
p2answer = sum(prod(v[i]-v[i-1]+1 for i in range(1,len(v),2) if v[i] > v[i-1])
               for v in [list(bound.values()) for bound in allowed_bounds])

print(f"The answer to part 1 is: {p1answer}")
print(f"The answer to part 2 is: {p2answer}")
