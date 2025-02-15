# https://adventofcode.com/2024/day/22

# Does the maths 2000 times according to the instructions for part 1
def process_secrets(num: int):
    for _ in range(2000):
        num = (num ^ num*64) % 16777216
        num = (num ^ int(num/32)) % 16777216
        num = (num ^ num*2048) % 16777216
    return num

# Gets a list of numbers
with open("input22.txt") as f:
    numbers = [int(line.strip()) for line in f.readlines()]


p1_answer = sum(process_secrets(x) for x in numbers)
print(f"The answer to part 1 is {p1_answer}")
p2_answer = 2
print(f"The answer to part 2 is {p2_answer}")
