import sys
import os

args = sys.argv[1:]

year, puzzle = args[0], args[1]

if not year.isnumeric() and not puzzle.isnumeric():
    sys.exit()

year, puzzle = int(year), int(puzzle)

code = f'''# https://adventofcode.com/{year}/day/{puzzle}

with open("inputtest.txt") as f:
    container = []
    for line in f.readlines():
        data = line.strip()

p1_answer = 1
print(f"The answer to part 1 is {{p1_answer}}")
p2_answer = 2
print(f"The answer to part 2 is {{p2_answer}}")
'''

try:
    os.chdir(f"../{year}")
except FileNotFoundError:
    os.mkdir(f"../{year}")
    os.chdir(f"../{year}")

if os.path.isfile(f"AoCDay{puzzle}.py"):
    print("This puzzle already exists, quitting")
    sys.exit()

with open(f"AoCDay{puzzle}.py", "+a") as f:
    f.write(code)