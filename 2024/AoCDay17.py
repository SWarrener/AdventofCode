# https://adventofcode.com/2024/day/17

# Get the value of the combo operands
def combo(reg, op):
    letters = {4: "A", 5: "B", 6: "C"}
    if op <= 3:
        return op
    return reg[letters[op]]

# Perform the division instructions
def division(reg, target: str, denominator: int):
    reg[target] = int(reg["A"]/ 2 ** combo(reg, denominator))

# Perform the bitwise instructions
def bitwise(reg, operand):
    reg["B"] = reg["B"] ^ operand

# Run the program, recording the output until the pointer is moved outside of the
# list of instructions
def run_program(reg, program, pointer = 0):
    output = []
    while pointer < len(program):
        opcode, operand = program[pointer], program[pointer+1]
        match opcode:
            case 0: division(reg, "A", operand)
            case 1: bitwise(reg, operand)
            case 2: reg["B"] = combo(reg, operand) % 8
            case 3: pointer = pointer if reg["A"] == 0 else operand - 2
            case 4: bitwise(reg, reg["C"])
            case 5: output.append(combo(reg, operand) % 8)
            case 6: division(reg, "B", operand)
            case 7: division(reg, "C", operand)
        pointer += 2
    return output

# Recursively build the number starting from the back of the input program. Try running
# the program with a value of a until you get the correct output. Then move on to the next
# digit in the input. Repeat until you have worked out all values of the input, and return that
# value of A
def find_a(target, a = 0, depth = 0):
    if depth == len(target):
        return a
    for i in range(8):
        output = run_program({"A": a*8 + i, "B":0, "C":0}, target[::-1])
        if output[0] == target[depth]:
            if result := find_a(target, (a*8 + i), depth + 1):
                return result
    return 0

# Extracts the instructions as a list of ints, and a dictionary for the register.
with open("input17.txt") as f:
    reg, program = {}, []
    for line in f.readlines():
        if "Reg" in line:
            reg[line[line.find(" ")+1:line.find(":")]] = int(line[line.find(":")+1:].strip())
        elif "Pro" in line:
            program = list(map(int, line[line.find(" "):].strip().split(",")))

p1_answer = ",".join(list(map(str, run_program(reg, program))))
print(f"The answer to part 1 is {p1_answer}")
p2_answer = find_a(program[::-1])
print(f"The answer to part 2 is {p2_answer}")
