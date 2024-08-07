def calcwinnings(num):
    value = 1
    for i in range(1, num):
        value *= 2
    return value

def createcopies(ori, num, copies):
    for i in range(1, num+1):
        new = i + ori
        if new <= 209:
            cards["Card"+str(new)][3] += 1*copies

with open("input4.txt") as f:
    cards = {}
    total = 0
    for line in f.readlines():
        #cards["Card 1"] = [winning numbers, card numbers, num of matches, num of copies]
        cards[line[:line.find(":")].replace(" ", "")] = [list(filter(None, line[line.find(":")+1:line.find("|")].split(" "))), list(filter(None,line[line.find("|")+1:-1].split(" ")))]
    for card in cards.values():
        winnings = 0
        for winner in card[0]:
            if winner in card[1]:
                winnings += 1
        card.append(winnings)
        card.append(1)
        if winnings > 0:
            total += calcwinnings(winnings)
    print(f"The answer to part 1 is: {total}")

    #part 2
    p2total = 0
    for k, v in cards.items():
        createcopies(int(k.replace("Card", "")), int(v[2]), v[3])
        p2total += v[3]
 
    print(f"The answer to part 2 is: {p2total}")

