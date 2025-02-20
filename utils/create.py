import sys
import os

args = sys.argv[1:]

year, puzzle, lang = args[0], args[1], args[2]

if not year.isnumeric() and not puzzle.isnumeric():
    sys.exit()

year, puzzle = int(year), int(puzzle)

code = ""

if args[2] == "py":
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

elif args[2] == "cs":
    code = f'''// https://adventofcode.com/{year}/day/{puzzle}

namespace CsharpAoC.Year{year}.Day{puzzle};

public class Solution: ISolver {{
    public string Part1(string[] input) {{
        return ""+1;
    }}

    public string Part1(string[] input) {{
        return ""+1;
    }}
}}
'''
    os.chdir("../CsharpAoC/bin")

try:
    os.chdir(f"../{year}")
except FileNotFoundError:
    os.mkdir(f"../{year}")
    os.chdir(f"../{year}")

if os.path.isfile(f"AoCDay{puzzle}.{args[2]}"):
    print("This puzzle already exists, quitting")
    sys.exit()

with open(f"AoCDay{puzzle}.{args[2]}", "+a") as f:
    f.write(code)
