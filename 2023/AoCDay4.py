# https://adventofcode.com/2023/day/4

# For each matching number increase the copies of the relevant card by the copies of the
# existing card
def createcopies(ori, num, copies):
    for i in range(1, num+1):
        new = i + ori
        if new <= 209:
            cards["Card"+str(new)][3] += 1*copies

# A dictionary of cards ["Card1"] = [winning numbers, card numbers, num of matches, num of copies]
# is extracted from the input. The filter is necessary due to extra spaces in the input. 
with open("input4.txt") as f:
    cards = {}
    for line in f.readlines():
        winning = list(filter(None, line[line.find(":")+1:line.find("|")].split(" ")))
        numbers = list(filter(None, line[line.find("|")+1:].strip().split(" ")))
        cards[line[:line.find(":")].replace(" ", "")] = [winning, numbers, 0, 1]

# For each card, if it has winnings, add 2 ^ (winnings - 1) to the answer
p1_answer = 0
for card in cards.values():
    card[2] = len([1 for x in card[0] if x in card[1]])
    if card[2] > 0:
        p1_answer += 2 ** (card[2] -1)
print(f"The answer to part 1 is: {p1_answer}")


# Find the number of copies of each card
p2_answer = 0
for k, v in cards.items():
    createcopies(int(k.replace("Card", "")), v[2], v[3])
    p2_answer += v[3]
print(f"The answer to part 2 is: {p2_answer}")
