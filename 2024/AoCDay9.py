# https://adventofcode.com/2024/day/9

# Creates a list of file id for file blocks and None for empty space
def create_fs(data):
    fs = [None if i % 2 == 1 else int(i/2) for i, char in enumerate(data) for _ in range(0, int(char))]
    return fs

# Moves the rightmost block to the first empty space and marks it as the end. Repeat until we run out
# of empty space
def move_blocks(fs):
    counter = 0
    while None in fs:
        fs[fs.index(None)] = fs[counter := counter - 1]
        fs[counter] = "E"
    return fs

with open("input9.txt") as f:
    for line in f.readlines():
        data = line.strip()

filesystem = create_fs(data)
filesystem = move_blocks(filesystem)

p1_answer = sum(i*num for i,num in enumerate(filesystem) if num != "E")
print(f"The answer to part 1 is {p1_answer}")
#p2_answer = 2
#print(f"The answer to part 2 is {p2_answer}")
