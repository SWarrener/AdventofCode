with open("input1.txt") as f: #part 1
    lines = f.readlines()
    total = 0
    for line in lines:
        if line != '\n':
            digit1 = 0
            digit2 = 0
            for char in line:
                try:
                    int(char)
                    digit1 = char
                    break
                except:
                    continue            
            for char in line[ : :-1]:
                try:
                    int(char)
                    digit2 = char
                    break
                except:
                    continue   
            num = int(digit1 + digit2)
            total += num
    print("The answer to part 1 is:", total)

def processline(line, back):
    lowestindex = 1000
    highestindex = -1
    index = 0
    digit = 0
    for item in searchitems:
        if back:
            index = line.rfind(item)
            if index != -1 and index > highestindex:
                highestindex = index
                digit = item
        else:
            index = line.find(item)
            if index != -1 and index < lowestindex:
                lowestindex = index
                digit = item
    if digit == "one":
        digit = "1"
    elif digit == "two":
        digit = "2"
    elif digit == "three":
        digit = "3"
    elif digit == "four":
        digit = "4"
    elif digit == "five":
        digit = "5"
    elif digit == "six":
        digit = "6"
    elif digit == "seven":
        digit = "7"
    elif digit == "eight":
        digit = "8"
    elif digit == "nine":
        digit = "9"
    return digit

with open("input1.txt") as f: #part 2
    lines = f.readlines()
    total = 0
    searchitems = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in lines:
        if line != '\n':
            digit1 = processline(line, False)
            digit2 = processline(line, True)
            num = int(digit1 + digit2)
            total += num
    print("The answer to part 2 is:", total)

