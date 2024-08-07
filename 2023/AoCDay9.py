def creatematrix(sequence):
    matrix = [sequence]
    while sequence.count(0) != len(sequence):
        sequence = [num-sequence[i-1] for i, num in enumerate(sequence) if i != 0]
        matrix.append(sequence)
    return matrix

def solvesequence1(sequence):
    matrix = creatematrix(sequence)
    temp = 0
    for step in reversed(matrix):
        if step.count(0) == len(step):
            continue
        step.append(temp+step[-1])
        temp = step[-1]
    return matrix[0][-1]

def solvesequence2(sequence):
    matrix = creatematrix(sequence)
    temp = 0
    for step in reversed(matrix):
        if step.count(0) == len(step):
            continue
        step.insert(0, step[0]-temp)
        temp = step[0]
    return matrix[0][0]

with open("input9.txt") as f:
    inputs = []
    for line in f.readlines():
        inputs.append([int(x) for x in line.strip().split(" ")])

p1answer = 0
p2answer = 0
for input in inputs:
    p1answer += solvesequence1(input)
    p2answer += solvesequence2(input)

print(f"The answer to part 1 is: {p1answer}")
print(f"The answer to part 2 is: {p2answer}")