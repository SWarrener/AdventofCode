from math import lcm

def SendSignals(destinations, new, type_, name):
    for target in destinations:
        new.append([target, type_, name])

def FModule(signal, new):
    module = modules[signal[0]]
    if signal[1] == "high":
        return
    if module["status"]:
        module["status"] = False
        SendSignals(module["destination"], new, "low", signal[0])
    else:
        module["status"] = True
        SendSignals(module["destination"], new, "high", signal[0])

def CModule(signal, new):
    module = modules[signal[0]]
    module["status"][signal[2]] = signal[1]
    for item in module["status"].values():
        if item == "low":
            SendSignals(module["destination"], new, "high", signal[0])
            return
    SendSignals(module["destination"], new, "low", signal[0])

def BModule(signal, new):
    module = modules[signal[0]]
    SendSignals(module["destination"], new, "low", signal[0])

def ProcessModules(modules):
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
                for signal in new_signals:
                    if signal[1] == "low":
                        signal_counts[1] += 1
                    if signal[1] == "high":
                        signal_counts[0] += 1
            signals = new_signals
        if iterations <= 1000:
            total_counts.append(signal_counts)
        iterations += 1
        if len(intervals) == len(periodics):
            break #  Assuming we hit all of them before hitting one twice
    return total_counts, intervals

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

for k, v in modules.items():
    if "rx" in v["destination"]:
        penultimate = k

for k, v in modules.items():
    if penultimate in v["destination"]:
        periodics.append(k)

total_counts, intervals = ProcessModules(modules)

p1answer = sum(x[0] for x in total_counts) * sum(x[1] for x in total_counts)
p2answer = lcm(*intervals)

print(f"The answer to part 1 is {p1answer}")
print(f"The answer to part 2 is {p2answer}")
