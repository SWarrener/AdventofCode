# https://adventofcode.com/2023/day/13

# Finds which two segments of the pattern exactly match each other, and returns the index of
# the match and True. Otherwise zero and False
def FindMatch(pattern):
    length = len(pattern)
    for i in range(int(length/2)):
        if pattern[:i+1] == list(reversed(pattern[i+1:i+i+2])):
            return i + 1, True
    count = 0
    for i in range(length-1, int(length/2), -1):
        count += 1
        if pattern[i:] == list(reversed(pattern[i-count:i])):
            return i, True
    return 0, False

# Returns True if lists A and B are the same and in the same order except for one character
# otherwise returns False
def FindChange(A, B):
    same = 1
    for i, _ in enumerate(A):
        if A[i] == B[i]:
            same += 1
    if same == len(A):
        return True
    return False

# Once we have found two rows next to each other that match, we need to check that there
# is one and only one change for the line of reflection to work. Iterates outwards from the
# match to confirm this, and returns True if it is the case, and false if it is not
def CompareTwo(pattern, i, changed = False):
    for j in range(1, int(len(pattern)/2)+1):
        try:
            if i-j < 0:
                raise IndexError
            x, y = pattern[i-j], pattern[i+1+j]
            if x == y:
                continue
            if abs(x.count('#') - y.count('#')) == 1 and not changed:
                if FindChange(x, y):
                    changed = True
                else:
                    break
            else:
                break
        except IndexError:
            if changed:
                return True
    return False

# Iterate through the neighbouring pairs of rows to dind matching, neighbouring lines
# to begin looking for a line of reflection. Also check to see if the change is on the
# neighbouring rows. Return the index of the reflection, True if it is found, 0, False if not
def FindSmudge(pattern, oldindex, axis):
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1] and not (i == oldindex and axis):
            if CompareTwo(pattern, i):
                return i+1, True
        elif FindChange(pattern[i], pattern[i+1]):
            if CompareTwo(pattern, i, True):
                return i+1, True
    return 0, False

# Takes each pattern and sees if there is a match in the horizontal axis. If not invert the grid
# and see if there is a match in the vertical axis. Add index to total and return once done.
# Additionally adds some data necessary for p2
def solve_p1(patterns):
    total = 0
    for x in patterns:
        pattern = x["grid"]
        tmp, match = FindMatch(pattern)
        total += 100*tmp
        x.update({"horizontal": match, "index": tmp}) # True is horizontal, False vertical
        if not match:
            pattern = [[pattern[j][i] for j in range(len(pattern))] for i in range(len(pattern[0]))]
            tmp, match = FindMatch(pattern)
            total += tmp
            x.update({"index": tmp})
    return total

# Takes each pattern and sees if there is a match in the horizontal axis. If not invert the grid
# and see if there is a match in the vertical axis. Add index to total and return once done.
def solve_p2(patterns):
    total = 0
    for x in patterns:
        pattern = x["grid"]
        tmp, match = FindSmudge(pattern, x["index"], x["horizontal"])
        total += 100*tmp
        if not match:
            pattern = [[pattern[j][i] for j in range(len(pattern))] for i in range(len(pattern[0]))]
            tmp, match = FindSmudge(pattern, x["index"], not x["horizontal"])
            total += tmp
    return total

# Extracts a list of pattern, where each pattern is a dictionary. Items represent the grid, but
# index and axis of match are added later.
with open("input13.txt") as f:
    patterns, temp = [], []
    for line in f.readlines():
        if line == "\n":
            patterns.append({"grid": temp})
            temp = []
        else:
            temp.append(list(line.strip()))

p1answer = solve_p1(patterns)
print(f"The answer to part 1 is {p1answer}")

p2answer = solve_p2(patterns)
print(f"The answer to part 2 is {p2answer}")
