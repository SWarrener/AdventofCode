# https://adventofcode.com/2024/day/5

# For each update take each number and check if the numbers behind and ahead of it are
# correct, if this is the case for all numbers in the update return True
def check_order(idx, num, update, orders):
    return all(update[j] in orders[num]["behind"] for j in range(0,idx)) and \
           all(update[j] in orders[num]["ahead"] for j in range(idx+1,len(update)-1))

# For each number find the count of numbers in the update it needs to be behind, and use that
# as the index for the reordered list
def reorder(update, orders):
    return sorted(update, key=lambda num: sum(1 if num in x["behind"] and k in update else 0 for k, x in orders.items()))

# Take each update, if it is in order, return the middle number, if it is not reorder and
# return the middle number
def solve(updates, orders, p1):
    for update in updates:
        if all(check_order(i, num, update, orders) for i, num in enumerate(update)) and p1:
            yield update[int(len(update)/2)]
        elif not all(check_order(i, num, update, orders) for i, num in enumerate(update)) and not p1:
            update = reorder(update, orders)
            yield update[int(len(update)/2)]


# Gets the updates and as a list of lists of ints. The data on where numbers must appear
# is a dict of dicts
with open("input5.txt") as f:
    orders= {}
    updates = []
    for line in f.readlines():
        if "|" in line:
            num1, num2 = int(line[:line.find("|")]), int(line[line.find("|")+1:])
            for num in (num1, num2):
                if num not in orders:
                    orders[num] = {"ahead": [], "behind": []} # This number must appear {} of others
            orders[num1]["ahead"].append(num2)
            orders[num2]["behind"].append(num1)
        elif "," in line:
            updates.append(list(map(int,line.strip().split(","))))

p1answer = sum(solve(updates, orders, True))
p2answer = sum(solve(updates, orders, False))

print(f"The answer to Part 1 is: {p1answer}")
print(f"The answer to Part 2 is: {p2answer}")
