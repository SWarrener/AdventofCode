# https://adventofcode.com/2024/day/9

# Creates a list of file id for file blocks and None for empty space
def create_fs(data):
    return [None if i % 2 == 1 else int(i/2) for i, char in enumerate(data) for _ in range(0, int(char))]

# Moves the rightmost block to the first empty space and marks it as the end. Repeat until we run out
# of empty space
def move_blocks(fs):
    counter = 0
    for i, char in enumerate(filesystem):
        if char is None:
            while fs[counter := counter - 1] is None:
                fs[counter] = "E"
            fs[i] = fs[counter]
            fs[counter] = "E"
    return fs

# Creates a list of lists of length of block and file id/None
def create_fs_2(data):
    return [[int(char),None] if i % 2 == 1 else [int(char),int(i/2)] for i,char in enumerate(data)]

# Moves the full blocks to the furthest left space which is available
def move_full_blocks(fs: list):
    i = 0
    for data in reversed(fs):
        i -= 1
        l, idx = data
        if idx is None:
            continue
        for i2, data2 in enumerate(fs[:i]):
            l2, idx2 = data2
            if idx2 is not None or l2 < l:
                continue
            fs[i2][0] -= l
            fs[i][1] = None
            i -= 1
            fs.insert(i2, [l, idx])
            break
    return fs

# Gets a single long string as the input
with open("input9.txt") as f:
    for line in f.readlines():
        data = line.strip()

filesystem = create_fs(data)
filesystem = move_blocks(filesystem)

p1_answer = sum(i*num for i,num in enumerate(filesystem) if num != "E")
print(f"The answer to part 1 is {p1_answer}")

filesystem = create_fs_2(data)
filesystem = move_full_blocks(filesystem)

counter = -1
p2_answer = sum((counter := counter +1)*idx if idx is not None else (counter := counter +1)*0
                 for l, idx in filesystem for _ in range (0,l))
print(f"The answer to part 2 is {p2_answer}")
