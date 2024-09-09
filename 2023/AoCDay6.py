#https://adventofcode.com/2023/day/6

# For each millisecond see if we beat the record distance, once we do subtract twice the value
# of the reach millisecond from the overall time. This + 1 is the number of milliseconds for which
# the distance is beaten, as the distance reached for each timestamp can be imagined as a symmetrical
# curve with its peak at time/2. 
def solve_race(time, distance):
    wincounter = 0
    for timestep in range(0, int(time/2)):
        tempdistance = timestep * (time-timestep)
        if tempdistance > distance:
            wincounter = time - (timestep*2)
            break
    return wincounter + 1

# Get the data into 2 lists, one for times and one for distances
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
    p1answer *= solve_race(times[i], distances[i])

print(f"The answer to part 1 is: {p1answer}")

p2time = int(''.join(map(str, times)))
p2distance = int(''.join(map(str, distances)))

p2answer = solve_race(p2time, p2distance)

print(f"The answer to part 2 is: {p2answer}")
