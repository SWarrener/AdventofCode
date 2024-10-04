#https://adventofcode.com/2023/day/20
from math import lcm

# Sends signals from a module to its destinations
def send_signals(destinations, new, type_, name):
    for target in destinations:
        new.append([target, type_, name])

# Processes an F module and deals with the logic of it sending signals
def FModule(signal, new):
    module = modules[signal[0]]
    if signal[1] == "high":
        return
    if module["status"]:
        module["status"] = False
        send_signals(module["destination"], new, "low", signal[0])
    else:
        module["status"] = True
        send_signals(module["destination"], new, "high", signal[0])

# Processes an C module and deals with the logic of it sending signals
def CModule(signal, new):
    module = modules[signal[0]]
    module["status"][signal[2]] = signal[1]
    for item in module["status"].values():
        if item == "low":
            send_signals(module["destination"], new, "high", signal[0])
            return
    send_signals(module["destination"], new, "low", signal[0])

# Processes the broadcast module and deals with the logic of it sending signals
def BModule(signal, new):
    module = modules[signal[0]]
    send_signals(module["destination"], new, "low", signal[0])

# Count the number of high and low signals for solving part 1
def count_signals(signals, counts):
    for signal in signals:
        if signal[1] == "low":
            counts[1] += 1
        if signal[1] == "high":
            counts[0] += 1
    return counts

# Deal with the logic of both parts in the same function as we can solve 1 on the way
# to solving 2. Each time we go through the while loop we start with sending one signal from
# the broadcast module, and it ends once we run out of signals. Once we have the 1000 button
# presses we store that as the answer to part 1 and once we have the iteration count for
# when the periodics we can solve part 2.
def process_modules(modules):
    iterations = 1
    total_counts = []
    intervals = []
    while iterations:
        signals = [["broadcaster", "low", None]] #  Target, Type, Origin
        signal_counts = [0, 1] #  High, Low
        while signals:
            new_signals = []
            for signal in signals:
                if signal[0] == "output" or signal[0] == "rx":
                    continue
                if signal[1] == "high" and signal[2] in periodics:
                    intervals.append(iterations)
                cur_type = modules[signal[0]]["type"]
                if cur_type == "B":
                    BModule(signal, new_signals)
                if cur_type == "F":
                    FModule(signal, new_signals)
                if cur_type == "C":
                    CModule(signal, new_signals)
            if iterations <= 1000:
                signal_counts = count_signals(new_signals, signal_counts)
            signals = new_signals
        if iterations <= 1000:
            total_counts.append(signal_counts)
        iterations += 1
        if len(intervals) == len(periodics):
            break #  Assuming we hit all of them before hitting one twice
    return total_counts, intervals

# Extracts a dictionary of dictionaries, where the name of the module is the key
# and the value is a dictionary of the type, destination and status of the module.
with open("input20.txt") as f:
    modules = {}
    for line in f.readlines():
        destination = line[line.find(">")+1:].strip().replace(" ", "").split(",")
        if line[0] == "%":
            name = line[line.find("%")+1:line.find(" ")]
            temp_type = "F"
            status = False #  Off, True would be On
        elif line[0] == "&":
            name = line[line.find("&")+1:line.find(" ")]
            temp_type = "C"
            status = {}
        elif line[0] == "b":
            name = line[:line.find(" ")]
            temp_type = "B"
            status = "low"
        modules[name] = {"type": temp_type, "destination":destination, "status":status}

for k, module in modules.items():
    if module["type"] == "C":
        for k1, module1 in modules.items():
            if k in module1["destination"]:
                module["status"][k1] = "low"

periodics, total_counts = [], []

# Find the end module, and then use that to find the penultimate module, and then that
# to find the antepenultimate ones. These ones (the periodics) are the ones we can do
# LCM maths on to solve part 2.
for k, v in modules.items():
    if "rx" in v["destination"]:
        penultimate = k

for k, v in modules.items():
    if penultimate in v["destination"]:
        periodics.append(k)

total_counts, intervals = process_modules(modules)

p1answer = sum(x[0] for x in total_counts) * sum(x[1] for x in total_counts)
p2answer = lcm(*intervals)

print(f"The answer to part 1 is {p1answer}")
print(f"The answer to part 2 is {p2answer}")
