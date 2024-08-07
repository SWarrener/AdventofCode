with open("input2.txt") as f: #part 1
    total = 0
    for line in f.readlines():
        gameid = int(line[line.find(" ")+1:line.find(":")])
        line = line[line.find(":")+1:]
        possible = True
        for game in line.split(";"):
            for colour in game.split(","):
                data = colour.strip().split(" ")
                num = int(data[0])
                colourid = data[1]
                if colourid == "green" and num > 13 or colourid == "red" and num > 12 or colourid == "blue" and num > 14:
                    possible = False
                    break
            if possible == False:
                break
        if possible == True:
            total += gameid
    print(f"The answer to part 1 is {total}")
        
with open("input2.txt") as f: #part 2
    total = 0
    for line in f.readlines():
        red = 0
        blue = 0
        green = 0
        line = line[line.find(":")+1:]
        for game in line.split(";"):
            for colour in game.split(","):
                data = colour.strip().split(" ")
                num = int(data[0])
                colourid = data[1]
                if colourid == "green" and num > green:
                    green = num
                elif colourid == "red" and num > red:
                    red = num
                elif colourid == "blue" and num > blue:
                    blue = num
        total += red*blue*green
    print(f"The answer to part 2 is {total}")            