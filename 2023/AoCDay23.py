# https://adventofcode.com/2023/day/23

# Check if coordinates are inside the grid, return True if that is the case
def inbounds(grid, x, y):
    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        return True
    return False

# Check that we are going the correct direction for any of the slopes, if we are return True
def try_special_character(char, direction):
    if char == ">" and direction == (0, 1):
        return True
    if char == "<" and direction == (0, -1):
        return True
    if char == "^" and direction == (-1, 0):
        return True
    if char == "v" and direction == (1, 0):
        return True
    return False

# Pathfind through the grid, yielding the length of all paths to the end.
def pathfind_p1(grid, start, end):
    open_list = [(0, *start, set())]
    while open_list:
        cur_length, cur_y, cur_x, closed_list = open_list.pop(0)
        if (cur_y, cur_x) in closed_list:
            continue
        if (cur_y, cur_x) == end:
            yield cur_length
        closed_list.add((cur_y, cur_x))
        for diff_y, diff_x in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            temp_y, temp_x = cur_y+diff_y, cur_x+diff_x
            if (temp_y, temp_x) in closed_list or not inbounds(grid, temp_x, temp_y):
                continue
            char = grid[temp_y][temp_x]
            if char == '#':
                continue
            if char == '.':
                open_list.append((cur_length+1, temp_y, temp_x, closed_list.copy()))
            else:
                if try_special_character(char, (diff_y, diff_x)):
                    open_list.append((cur_length+1, temp_y, temp_x, closed_list.copy()))
                else:
                    continue

# Check if a tile is surrounded by special characters, if it is then the tile is a node
def detect_node(grid, coords):
    cur_y, cur_x = coords
    count = 0
    for diff_y, diff_x in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if grid[cur_y+diff_y][cur_x+diff_x] in (">", "<", "^", "v"):
            count += 1
    if count >= 2:
        return count
    return 0

# Find node with the given the coords and return its name, or None if it doesn't exist
def find_node_by_coords(nodes, coords):
    for k, node in nodes.items():
        if node["coords"] == coords:
            return k
    return None

# Find the nodes, and make a dictionary of their coords and how many paths there are
def find_nodes(grid, start, end):
    nodes = {"start": {"coords": start, "paths": 1, "neighbours": []}}
    node_count = 1
    open_list = [(0, *start)]
    closed_list = set()
    while open_list:
        cur_length, cur_y, cur_x = open_list.pop(0)
        if (cur_y, cur_x) in closed_list:
            continue
        if (cur_y, cur_x) == end:
            nodes["end"] = {"coords": end, "paths": 1, "neighbours": []}
        closed_list.add((cur_y, cur_x))
        for diff_y, diff_x in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            temp_y, temp_x = cur_y+diff_y, cur_x+diff_x
            if (temp_y, temp_x) in closed_list or not inbounds(grid, temp_x, temp_y):
                continue
            char = grid[temp_y][temp_x]
            if char == '#':
                continue
            if char == ".":
                open_list.append((cur_length+1, temp_y, temp_x))
            elif char in (">", "<", "^", "v"):
                open_list.append((cur_length+1, temp_y, temp_x))
                temp_y, temp_x = temp_y+diff_y, temp_x+diff_x
                if (count := detect_node(grid, (temp_y, temp_x))):
                    if not find_node_by_coords(nodes, (temp_y, temp_x)):
                        nodes[str(node_count)] = {"coords": (temp_y, temp_x), "paths": count, "neighbours": []}
                        node_count += 1
    return nodes

# Find which nodes neighbour a given node, and the distance to them
def find_node_neighbours(grid, node, end_coords):
    open_list = [(0, *node["coords"])]
    closed_list = set()
    while len(node["neighbours"]) < node["paths"]:
        cur_length, cur_y, cur_x = open_list.pop(0)
        if (cur_y, cur_x) in closed_list:
            continue
        if (cur_y, cur_x) in end_coords and (cur_y, cur_x) != node["coords"]:
            node["neighbours"].append((cur_length, find_node_by_coords(nodes, (cur_y, cur_x))))
            continue
        closed_list.add((cur_y, cur_x))
        for diff_y, diff_x in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            temp_y, temp_x = cur_y+diff_y, cur_x+diff_x
            if (temp_y, temp_x) in closed_list or not inbounds(grid, temp_x, temp_y):
                continue
            char = grid[temp_y][temp_x]
            if char == '#':
                continue
            open_list.append((cur_length+1, temp_y, temp_x))

# Link the nodes to their neighbours
def link_nodes(grid, nodes):
    node_coords = [node["coords"] for node in nodes.values()]
    for node in nodes.values():
        find_node_neighbours(grid, node, node_coords)


# Pathfind through the nodes and yield lengths of paths from the start to the end.
def pathfind_nodes(nodes):
    open_list = [(0, "start", set())]
    while open_list:
        cur_length, cur_node, closed_list = open_list.pop()
        if cur_node in closed_list:
            continue
        if cur_node == "end":
            yield cur_length
        closed_list.add(cur_node)
        for path in nodes[cur_node]["neighbours"]:
            temp_length, temp_node = path
            if temp_node in closed_list:
                continue
            open_list.append((temp_length+cur_length, temp_node, closed_list.copy()))

# Extracts a list of lists representing the grid
with open("input23.txt") as f:
    grid = []
    for line in f.readlines():
        grid.append(list(line.strip()))

start = (0, grid[0].index("."))
end = (len(grid)-1, grid[-1].index("."))

p1answer = max(pathfind_p1(grid, start, end))
print(f"The answer to part 1 is {p1answer}")

nodes = find_nodes(grid, start, end)
link_nodes(grid, nodes)

p2answer = max(pathfind_nodes(nodes))
print(f"The answer to part 2 is {p2answer}")
