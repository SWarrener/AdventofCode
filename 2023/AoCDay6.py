with open("input6.txt") as f:
    times = []
    distances = []
    for line in f.readlines():
        if line[0] == "T":
            times = [int(x) for x in line[line.find(":")+1:].strip().split(" ") if x]
        elif line[0] == "D":
            distances = [int(x) for x in line[line.find(":")+1:].strip().split(" ") if x]

p1answer = 1

for i in range(0, len(times)):
    wincounter = 0
    for timestep in range(0, times[i]):
        tempdistance = timestep * (times[i]-timestep)
        if tempdistance > distances[i]:
            wincounter += 1
    p1answer *= wincounter

print(f"The answer to part 1 is: {p1answer}")

p2time = int(''.join(map(str, times)))
p2distance = int(''.join(map(str, distances)))
wincounter2 = 0

for timestep in range(0, int(p2time/2)):
    tempdistance = timestep * (p2time-timestep)
    if tempdistance > p2distance:
        wincounter2 += 1

print(f"The answer to part 2 is: {wincounter2*2+1}")