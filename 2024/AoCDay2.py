# https://adventofcode.com/2024/day/2

# Take the list and check if any numbers are out of order or have an invalid difference
def solve(report: list):
    for i in range(len(report)-1):
        if abs(report[i] - report[i+1]) >= 4 or abs(report[i] - report[i+1]) == 0:
            return 0
    ascending = report[0] - report[-1] < 0
    for i in range(len(report)-1):
        if ascending and report[i] - report[i+1] >= 0:
            return 0
        if not ascending and report[i] - report[i+1] <= 0:
            return 0
    return 1

# Test removing each value from the list and see if that new list is valid.
# Could be optimised a bit, but runs instantly on my PC anyway.
def solvep2(report: list):
    temp = report.copy()
    total = []
    for i in range(len(report)):
        del report[i]
        total.append(solve(report))
        report = temp.copy()
    return any(total)

# Gets a list of lists of numbers
with open("input2.txt") as f:
    reports = []
    for line in f.readlines():
        reports.append(list(map(int, line.strip().split(" "))))

p1answer = sum(solve(x) for x in reports)
p2answer = sum(solvep2(x) for x in reports)

print(f"The answer to part 1 is: {p1answer}")
print(f"The answer to part 2 is: {p2answer}")
