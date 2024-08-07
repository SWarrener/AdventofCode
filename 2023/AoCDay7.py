#Commented out for part 1 

#def comparestrength(A, B): #1 A is higher, 0 B is higher
#    for x, y in zip(A, B):
#        if x == y:
#            continue
#        if strength.index(x) < strength.index(y):
#            return 1
#        else:
#            return 0

#def solvehand(A):
#    counts = [A.count(A[x]) for x in range(0, len(A))]
#    if counts.count(5) == 5:
#        return 0
#    elif counts.count(4) == 4:
#        return 1
#    elif counts.count(3) == 3: 
  #      if counts.count(2) == 2:
 #           return 2
 #       else:
 #           return 3
#    elif counts.count(2) == 4:
#        return 4
#    elif counts.count(2) == 2:
#        return 5
#    else:
#        return 6
    
#def comparehands(A, B): #1 A is higher, 0 B is higher
#    if solvehand(A) < solvehand(B):
#        return 1
#    elif solvehand(B) < solvehand(A):
#        return 0
#    else:
#        return comparestrength(A, B)

#with open("input7.txt") as f:
#    cards = []
#    strength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
#    for line in f.readlines():
 #       cards.append({"value": list(line[:line.find(" ")]), "bid": int(line[line.find(" ")+1:].strip())})
#
#p1answer = 0
#
#for card in cards:
#    score = 1
#    for cardb in cards:
#        if card == cardb:
#            continue
#        score += comparehands(card["value"], cardb["value"])
#    card["score"] = score
#   p1answer += score*card["bid"]
#
#print(f"The answer to part 1 is: {p1answer}")

def comparestrength(A, B): #1 A is higher, 0 B is higher
    for x, y in zip(A, B):
        if x == y:
            continue
        if strength.index(x) < strength.index(y):
            return 1
        else:
            return 0

def solvehand(A):
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
    
def comparehands(A, B): #1 A is higher, 0 B is higher
    if solvehand(A) < solvehand(B):
        return 1
    elif solvehand(B) < solvehand(A):
        return 0
    else:
        return comparestrength(A, B)

with open("input7.txt") as f:
    cards = []
    strength = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    for line in f.readlines():
        cards.append({"value": list(line[:line.find(" ")]), "bid": int(line[line.find(" ")+1:].strip())})

p2answer = 0

for card in cards:
    score = 1
    for cardb in cards:
        if card == cardb:
            continue
        score += comparehands(card["value"], cardb["value"])
    card["score"] = score
    p2answer += score*card["bid"]

print(f"The answer to part 2 is: {p2answer}")