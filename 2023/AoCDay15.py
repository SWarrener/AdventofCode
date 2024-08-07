def CalcHash(string):
    answer = 0
    for code in string.encode('ascii'):
        answer = ((answer + code)*17) % 256
    return answer

def FindLens(box, string):
    for i, lens in enumerate(box):
        if lens[0] == string:
            return i
    return -1

with open("input15.txt") as f:
    for line in f.readlines():
        strings = line.strip().split(",")

p1answer = sum([CalcHash(string) for string in strings])

print(f"The answer to part 1 is: {p1answer}")

lenses = [[string[:-1], '-'] if '-' in string else 
        [string[:string.find('=')], "=", string[-1]] for string in strings]

boxes = [[] for _ in range(256)]

for lens in lenses:
    box_num = CalcHash(lens[0])
    temp = FindLens(boxes[box_num], lens[0])
    if lens[1] == '-':
        if temp != -1: boxes[box_num].pop(temp)
    if lens[1] == "=":
        if temp == -1:
            boxes[box_num].append([lens[0], lens[2]])
        else:
            boxes[box_num][temp] = [lens[0], lens[2]]

p2answer = sum([(1+i)*(1+j)*int(lens[1]) for i, box in enumerate(boxes) for j, lens in enumerate(box)])

print(f"The answer to part 1 is: {p2answer}")