input = []

with open("input.txt") as f:
    input = [list(line) for line in f.read().strip().split("\n")]

def equal(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return False

    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] != b[i][j]:
                return False    
    return True

# --- Part 1 ---

last_layout = []
current_layout = [x.copy() for x in input]

while not equal(last_layout, current_layout):
    to_empty = []
    to_occupy = []

    for i in range(len(current_layout)):
        for j in range(len(current_layout[i])):
            if current_layout[i][j] != ".":
                adjacents = [(i-1, j-1), (i-1,j), (i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
                occupied = 0
                for y, x in adjacents:
                    if y >= 0 and y < len(current_layout) and x >= 0 and x < len(current_layout[i]):

                        if current_layout[y][x] == "#":
                            occupied += 1
                
                if current_layout[i][j] == "L" and occupied == 0:
                    to_occupy.append((i, j))
                elif current_layout[i][j] == "#" and occupied >= 4:
                    to_empty.append((i, j))
    
    last_layout = [x.copy() for x in current_layout]
    for i, j in to_empty:
        current_layout[i][j] = "L"
    for i, j in to_occupy:
        current_layout[i][j] = "#"


part1 = 0
for i in range(len(current_layout)):
    for j in range(len(current_layout[i])):
        if current_layout[i][j] == "#":
            part1 += 1

print(part1)

# --- Part 2 ---

def in_bounds(coord, layout):
    y, x = coord
    return y >= 0 and y < len(layout) and x >= 0 and x < len(layout[y])

def check_direction(start, delta, layout):
    pos = (start[0]+delta[0], start[1]+delta[1])
    while in_bounds(pos, layout):
        if layout[pos[0]][pos[1]] == "#":
            return True
        elif layout[pos[0]][pos[1]] == "L":
            return False

        pos = (pos[0]+delta[0], pos[1]+delta[1])
    
    return False


last_layout = []
current_layout = [x.copy() for x in input]

while not equal(last_layout, current_layout):
    to_empty = []
    to_occupy = []

    for i in range(len(current_layout)):
        for j in range(len(current_layout[i])):
            if current_layout[i][j] != ".":
                deltas = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]
                occupied = 0
                for delta in deltas:
                    occupied += 1 if check_direction((i, j), delta, current_layout) else 0
                
                if current_layout[i][j] == "L" and occupied == 0:
                    to_occupy.append((i, j))
                elif current_layout[i][j] == "#" and occupied >= 5:
                    to_empty.append((i, j))
    
    last_layout = [x.copy() for x in current_layout]
    for i, j in to_empty:
        current_layout[i][j] = "L"
    for i, j in to_occupy:
        current_layout[i][j] = "#"


part2 = 0
for i in range(len(current_layout)):
    for j in range(len(current_layout[i])):
        if current_layout[i][j] == "#":
            part2 += 1

print(part2)
