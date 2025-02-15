# https://adventofcode.com/2024/day/22

# Does the maths 2000 times according to the instructions for part 1
def process_secrets(num: int):
    result = [num]
    for _ in range(2000):
        num = (num ^ num*64) % 16777216
        num = (num ^ int(num/32)) % 16777216
        num = (num ^ num*2048) % 16777216
        result.append(num)
    return result

# First find the last digit of each secret number, then create another nested list of the changes between them.
# Use these two nested lists to make a dictionary of each 4 digit set of changes and the total number of bananas
# that would give. Return the highest value in that dictionary.
def count_changes(secrets: list):
    last_digits = [[x%10 for x in sub] for sub in secrets]
    changes = [[sub[i+1] - num for i, num in enumerate(sub[:-1])] for sub in last_digits]
    totals = {}
    for j, sub in enumerate(changes):
        used = set()
        for i in range(3, 2000):
            change_list = tuple(sub[i-3:i+1])
            if change_list in used: # Ensures that only the first number for each set of digits is considered
                continue
            used.add(change_list)
            if change_list not in totals:
                totals[change_list] = last_digits[j][i+1]
            else:
                totals[change_list] += last_digits[j][i+1]
    return max(totals.values())

# Gets a list of numbers
with open("input22.txt") as f:
    numbers = [int(line.strip()) for line in f.readlines()]

secrets = [process_secrets(x) for x in numbers]

p1_answer = sum(x[-1] for x in secrets)
print(f"The answer to part 1 is {p1_answer}")
p2_answer = count_changes(secrets)
print(f"The answer to part 2 is {p2_answer}")
