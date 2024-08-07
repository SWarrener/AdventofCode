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

def FindChange(A, B):
    same = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            same += 1
    if same + 1 == len(A):
        return True
    return False

def CompareTwo(pattern, i, changed = False):
    for j in range(1, int(len(pattern)/2)+1):
        try:
            if i-j < 0:
                raise IndexError
            x, y = pattern[i-j], pattern[i+1+j]
            if x == y:
                continue
            elif abs(x.count('#') - y.count('#')) == 1 and not changed:
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

def FindSmudge(pattern, oldindex, axis):
    
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1] and not (i == oldindex and axis):
            if CompareTwo(pattern, i):
                return i+1, True
        elif FindChange(pattern[i], pattern[i+1]):
            if CompareTwo(pattern, i, True):
                return i+1, True

    return 0, False

with open("input13.txt") as f:
    patterns, temp = [], []
    for line in f.readlines():
        if line == "\n":
            patterns.append({"grid": temp})
            temp = []
        else:
            temp.append(list(line.strip()))

p1answer = 0

for x in patterns:
    pattern = x["grid"]
    tmp, match = FindMatch(pattern)
    p1answer += 100*tmp
    x.update({"horizontal": match, "index": tmp}) #True is horizontal, False vertical
    if not match:
        pattern = [[pattern[j][i] for j in range(len(pattern))] for i in range(len(pattern[0]))]
        tmp, match = FindMatch(pattern)
        p1answer += tmp
        x.update({"index": tmp})

print(f"The answer to part 1 is {p1answer}")

p2answer = 0

for x in patterns:
    pattern = x["grid"]
    tmp, match = FindSmudge(pattern, x["index"], x["horizontal"])
    p2answer += 100*tmp
    if not match:
        pattern = [[pattern[j][i] for j in range(len(pattern))] for i in range(len(pattern[0]))]
        tmp, match = FindSmudge(pattern, x["index"], not x["horizontal"])
        p2answer += tmp

print(f"The answer to part 2 is {p2answer}")
