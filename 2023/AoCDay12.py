from functools import cache

@cache
def recursive(springs, nums, result = 0):
    if not nums:
        return '#' not in springs
    cur, nums = nums[0], nums[1:]
    for i in range(len(springs) - sum(nums) - len(nums) - cur + 1):
        if '#' in springs[:i]:
            break
        if (nxt := i+cur) <= len(springs) and '.' not in springs[i:nxt] and springs[nxt:nxt+1] != '#':
            result += recursive(springs[nxt+1:], nums)
    return result

with open("input12.txt") as f:
    Records = []
    for line in f.readlines():
        Records.append({"Springs": line[:line.find(" ")].strip(), "nums": tuple(map(int, line[line.find(" "):].strip().split(",")))})

p1answer, p2answer = 0, 0

for line in Records:
    p1answer += recursive(line["Springs"], line["nums"])
    p2answer += recursive("?".join([line["Springs"]]*5), line["nums"]*5)

print(f"The answer to part 1 is: {p1answer}")
print(f"The answer to part 2 is: {p2answer}")