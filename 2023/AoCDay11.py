#Old p1 answer, neater one below
#def AddSpace(matrix):
#    
#    rows = [i for i, line in enumerate(matrix) if '#' not in line]      
#    for i, index in enumerate(rows):
#        matrix.insert(index+i, ['.' for _ in range(len(matrix[0]))])
#
#    matrix = [[matrix[j][i] for j, _ in enumerate(matrix)] for i in range(len(matrix[0]))]
#    
#    rows = [i for i, line in enumerate(matrix) if '#' not in line]      
#    for i, index in enumerate(rows):
#        matrix.insert(index+i, ['.' for _ in range(len(matrix[0]))])#
#
#    return [[matrix[j][i] for j, _ in enumerate(matrix)] for i in range(len(matrix[0]))]

#def FindCoords(matrix):
#    coords = []
#    for i, line in enumerate(matrix):
#        for j, char in enumerate(line):
#            if char == '#':
#                coords.append((j, i))
#    return coords

#with open("input11.txt") as f:
#    matrix = []
#    for line in f.readlines():
#        matrix.append(list(line.strip()))

#matrix = AddSpace(matrix)

#coords = FindCoords(matrix)

#pairs = [(coords[i], coords[j]) for i in range(len(coords)) for j in range(i+1, len(coords))]

#p1answer = 0

#print(f"The answer to part 1 is: {p1answer}")

def FindEmpty(matrix):
    rows = [i for i, line in enumerate(matrix) if '#' not in line]      
    matrix = [[matrix[j][i] for j, _ in enumerate(matrix)] for i in range(len(matrix[0]))]
    columns = [i for i, line in enumerate(matrix) if '#' not in line]
    return {"rows":rows, "columns": columns}

def FindCoords(matrix):
    coords = []
    for i, line in enumerate(matrix):
        for j, char in enumerate(line):
            if char == '#':
                coords.append((j, i))
    return coords

def CalcDistance(pairs, emptylists, emptyaddition):
    total = 0
    for pair in pairs:
        Ax = pair[0][0]
        Bx = pair[1][0]
        Ay = pair[0][1]
        By = pair[1][1]
        total += abs(Ax - Bx)
        total += abs(Ay - By)
        for i in emptylists["columns"]:
            if i<Ax and i>Bx or i<Bx and i>Ax:
                total+= emptyaddition
        for i in emptylists["rows"]:
            if i<Ay and i>By or i<By and i>Ay:
                total+= emptyaddition
    return total

with open("input11.txt") as f:
    matrix = []
    for line in f.readlines():
        matrix.append(list(line.strip()))

empty = FindEmpty(matrix)
coords = FindCoords(matrix)
pairs = [(coords[i], coords[j]) for i in range(len(coords)) for j in range(i+1, len(coords))]

p1answer = CalcDistance(pairs, empty, 1)
print(f"The answer to part 1 is: {p1answer}")

p2answer = CalcDistance(pairs, empty, 999999)
print(f"The answer to part 2 is: {p2answer}")