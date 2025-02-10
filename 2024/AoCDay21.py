# https://adventofcode.com/2024/day/21

# Take the manhattan distance from where we are to where we are going, and add the instructions
# together according to specified logic to ensure that we always pick the shortest sequence of
# instructions
def pathfind(code: str):
    for j in range(3):
        if j == 0:
            keypad = {"7": (0,0), "8": (0,1), "9": (0,2), "4": (1,0), "5": (1,1), "6": (1,2),
           "1": (2,0), "2": (2,1), "3": (2,2), "0": (3,1), "A": (3,2)}
        else:
            keypad = {"^": (0,1), "A": (0,2), "<": (1,0), "v": (1,1), ">": (1,2)}
        output = []
        loc = "A"
        for next_ in code:
            c_coords, n_coords = keypad[loc], keypad[next_]
            man_y, man_x = tuple(n_coords[i] - c_coords[i] for i in range(len(c_coords)))
            updo = ["v" if man_y > 0 else "^" for _ in range(abs(man_y))]
            leri = [">" if man_x > 0 else "<" for _ in range(abs(man_x))]
            if j == 0 and c_coords[0] == 3 and n_coords[1] == 0:
                step = updo + leri
            elif j == 0 and c_coords[1] == 0 and n_coords[0] == 3:
                step = leri + updo
            elif j > 0 and c_coords == (1,0):
                step = leri + updo
            elif j > 0 and n_coords == (1,0):
                step = updo + leri
            elif man_x < 0:
                step = leri + updo
            else:
                step = updo + leri
            output += step + ["A"]
            loc = next_
        code = output
    return len(output)

# Get a list of the codes
with open("input21.txt") as f:
    codes = [line.strip() for line in f.readlines()]

p1_answer = sum(int(code.strip("A")) * pathfind(code) for code in codes)
print(f"The answer to part 1 is {p1_answer}")
p2_answer = 2
print(f"The answer to part 2 is {p2_answer}")
