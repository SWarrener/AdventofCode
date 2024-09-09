# https://adventofcode.com/2023/day/7

# Work out which type the hand is, and return a score based on that
def solvehand_1(A):
    counts = [A.count(A[x]) for x in range(0, len(A))]
    if counts.count(5) == 5:
        return 0
    elif counts.count(4) == 4:
        return 1
    elif counts.count(3) == 3: 
        if counts.count(2) == 2:
            return 2
        else:
            return 3
    elif counts.count(2) == 4:
        return 4
    elif counts.count(2) == 2:
        return 5
    else:
        return 6

# If the types match then work out which hand is stronger and return based on that
def comparestrength(A, B): #1 A is higher, 0 B is higher
    for x, y in zip(A, B):
        if x == y:
            continue
        if strength.index(x) < strength.index(y):
            return 1
        else:
            return 0

# Work out which type the hand is for part 2, accounting for the joker cards. 
def solvehand_2(A):
    counts = [A.count(A[x]) if A[x] != "J" else 0 for x in range(0, len(A))]
    counts.sort(reverse=True)
    counts[:counts.count(counts[0])] = [counts[0] + A.count("J")] * counts.count(counts[0])
    if 5 in counts:
        return 0
    elif 4 in counts:
        return 1
    elif 3 in counts: 
        if 2 in counts or counts.count(3) == 4 and A.count("J") == 1:
            return 2
        else:
            return 3
    elif counts.count(2) == 4 and A.count("J") == 0:
        return 4
    elif counts.count(2) == 2 or A.count("J") == 1:
        return 5
    else:
        return 6

# Compare two hands and work out which is stronger. 
def comparehands(A, B, function): #1 A is higher, 0 B is higher
    A_score, B_score = function(A), function(B)
    if A_score < B_score:
        return 1
    elif B_score < A_score:
        return 0
    else:
        return comparestrength(A, B)

# Get a list of dictionaries for each card 
with open("input7.txt") as f:
    cards = []
    for line in f.readlines():
        cards.append({"value": list(line[:line.find(" ")]), 
                      "bid": int(line[line.find(" ")+1:].strip()), 
                      "score": 1})

# Process part 1 
strength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
p1answer = 0
for card in cards:
    card["score"] += sum([comparehands(card["value"], cardb["value"], solvehand_1)
                          for cardb in cards if card != cardb])
    p1answer += card["score"]*card["bid"]

print(f"The answer to part 1 is: {p1answer}")

# Process part 2
strength = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
p2answer = 0
for card in cards:
    card["score"] = 1
    card["score"] += sum([comparehands(card["value"], cardb["value"], solvehand_2)
                          for cardb in cards if card != cardb])
    p2answer += card["score"]*card["bid"]

print(f"The answer to part 2 is: {p2answer}")
