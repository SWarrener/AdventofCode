# https://adventofcode.com/2023/day/2

# For each round in each game check if it is possible. Any colour having above the 
# specified number is impossible. Sum ids of possible games and return.
def calculate_p1(games):
    total = 0
    for gameid, game in games:
        possible = True
        for round in game:
            for colour in round.split(","):
                data = colour.strip().split(" ")
                num = int(data[0])
                colourid = data[1]
                if colourid == "green" and num > 13 or colourid == "red" and num > 12 or colourid == "blue" and num > 14:
                    possible = False
                    break
            if not possible: break
        if possible:
            total += gameid
    return total

# For each game find the largest value of red blue and green needed by any individual round.
# times them together and return the sum of this value for all games.
def calculate_p2(games):
    total = 0
    for _, game in games:
        red, blue, green = 0, 0, 0
        for round in game:
            for colour in round.split(","):
                num, colourid = tuple(colour.strip().split(" "))
                num = int(num)
                if colourid == "green" and num > green:
                    green = num
                elif colourid == "red" and num > red:
                    red = num
                elif colourid == "blue" and num > blue:
                    blue = num
        total += red*blue*green
    return total

# A list of (gameids, game data) is extracted from the input
with open("input2.txt") as f:
    games = []
    for line in f.readlines():
        gameid = int(line[line.find(" ")+1:line.find(":")])
        game = line[line.find(":")+1:].strip().split(";")
        games.append((gameid, game))

# Run the functions and print the answers. 
p1_answer = calculate_p1(games)
print(f"The answer to part 1 is {p1_answer}")

p2_answer = calculate_p2(games)
print(f"The answer to part 2 is {p2_answer}")
