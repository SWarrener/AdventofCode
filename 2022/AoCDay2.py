# https://adventofcode.com/2022/day/2

# Use the dictionaries to add the score for what we played and the score for the outcome
def solve_p1(hands):
    return sum(p1_scores[us] + wins[them+us] for them, us in hands)

# Use the list as a lookup table for the score. The index of the pairs is the score that combo will give
def solve_p2(hands):
    return sum(p2_scores.index(them+us) for them, us in hands)

# Gets a list of tuples representing the hands
with open("input2.txt") as f:
    hands = [(line[0], line[2]) for line in f.readlines()]

p1_scores = {"X": 1, "Y": 2, "Z": 3}
wins = {"AX": 3, "BX": 0, "CX": 6, "AY": 6, "BY": 3, "CY": 0, "AZ": 0, "BZ": 6, "CZ": 3}
p2_scores = ["", "BX", "CX", "AX", "AY", "BY", "CY", "CZ", "AZ", "BZ"]

p1_answer = solve_p1(hands)
print(f"The answer to part 1 is {p1_answer}")
p2_answer = solve_p2(hands)
print(f"The answer to part 2 is {p2_answer}")
