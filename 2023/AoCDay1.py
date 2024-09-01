# https://adventofcode.com/2023/day/1

# For the line iterate from the front and back until we find the first
# number in each case, combine them (so 5 and 7 become 57) and return.
def process_p1(line):
    for char in line:
        if char.isdigit():
            digit_1 = char
            break          
    for char in reversed(line):
        if char.isdigit():
            digit_2 = char
            break   
    return int(digit_1 + digit_2)

# Find the items from search items that have the lowest and highest idex value for the line. 
# Get it into numeric string from, combine the two digits, and return them. 
def process_p2(line):
    text_to_number = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", 
                      "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    search_items = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", 
                    "three", "four", "five", "six", "seven", "eight", "nine"]

    left_data = min((line.find(x), i) for i, x in enumerate(search_items) if line.find(x) != -1)
    digit_1 = search_items[left_data[1]]
    right_data = max((line.rfind(x), i) for i, x in enumerate(search_items) if line.rfind(x) != -1)
    digit_2 = search_items[right_data[1]]

    if digit_2 in text_to_number.keys():
        digit_2 = text_to_number[digit_2]
    if digit_1 in text_to_number.keys():
        digit_1 = text_to_number[digit_1]

    return int(digit_1 + digit_2)

with open("input1.txt") as f:
    data = []
    for line in f.readlines():
        data.append(line.strip())

# Sum the answer from each line and then print that as the answer
p1_answer = sum(process_p1(line) for line in data)
print("The answer to part 1 is:", p1_answer)

p2_answer = sum(process_p2(line) for line in data)
print("The answer to part 2 is:", p2_answer)
