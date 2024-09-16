# https://adventofcode.com/2023/day/9

# Create a list of lists, where each list is a sequence of differences between the numbers
# in the sequence above it in the list. Exit and return the whole list of lists once we have
# a list consisting entirely of zeroes.
def creatematrix(sequence):
    matrix = [sequence]
    while sequence.count(0) != len(sequence):
        sequence = [num-sequence[i-1] for i, num in enumerate(sequence) if i != 0]
        matrix.append(sequence)
    return matrix


# Go back through the matrix and sum the last value to the last value of the sequence above.
# Contrinue the process until you get to the original sequence and have calculated the expected next
# value. Return that value.
def solvesequence1(matrix):
    temp = 0
    for step in reversed(matrix):
        if step.count(0) == len(step):
            continue
        step.append(temp+step[-1])
        temp = step[-1]
    return matrix[0][-1]


# Similar to the above function, go back through the matrix, and sum the first value to the first value
# of the sequence above. Continue until the you have the original sequence and have calculated the expected
# previous value. return that value
def solvesequence2(matrix):
    temp = 0
    for step in reversed(matrix):
        if step.count(0) == len(step):
            continue
        step.insert(0, step[0]-temp)
        temp = step[0]
    return matrix[0][0]


# Get a list of numbers per line
with open("input9.txt") as f:
    data = []
    for line in f.readlines():
        data.append([int(x) for x in line.strip().split(" ")])


# Use the above functions to caluclate the result, as we don't edit the inputs we can do both parts
# to the puzzle in the same loop. Finally, print the answers
p1answer = 0
p2answer = 0
for line in data:
    matrix = creatematrix(line)
    p1answer += solvesequence1(matrix)
    p2answer += solvesequence2(matrix)

print(f"The answer to part 1 is: {p1answer}")
print(f"The answer to part 2 is: {p2answer}")
