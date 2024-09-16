# https://adventofcode.com/2023/day/2

# For each round in each game check if it is possible. Any colour having above the
# specified number is impossible. Sum ids of possible games and return.
def calculate_p1(games):
    total = 0
    for id_, game in games:
        possible = True
        for round_ in game:
            for colour in round_.split(","):
                data = colour.strip().split(" ")
                num = int(data[0])
                colourid = data[1]
                if any(colour == colourid and num > x for colour, x in (("green", 13),("red", 12),("blue", 14))):
                    possible = False
                    break
            if not possible:
                break
        if possible:
            total += id_
    return total

# For each game find the largest value of red blue and green needed by any individual round.
# times them together and return the sum of this value for all games.
def calculate_p2(games):
    total = 0
    for _, game in games:
        red, blue, green = 0, 0, 0
        for round_ in game:
            for colour in round_.split(","):
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
    games_list = []
    for line in f.readlines():
        game_id = int(line[line.find(" ")+1:line.find(":")])
        game_data = line[line.find(":")+1:].strip().split(";")
        games_list.append((game_id, game_data))

# Run the functions and print the answers.
p1_answer = calculate_p1(games_list)
print(f"The answer to part 1 is {p1_answer}")

p2_answer = calculate_p2(games_list)
print(f"The answer to part 2 is {p2_answer}")
