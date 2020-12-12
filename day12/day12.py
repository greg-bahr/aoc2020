input = []

with open("input.txt") as f:
    input = f.read().strip().split("\n")

# --- Part 1 ---

pos = [0, 0]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
current_direction = 1

for instruction in input:
    direction = instruction[0]
    num = int(instruction[1:])

    if direction == "N":
        pos[1] += num
    elif direction == "S":
        pos[1] -= num
    elif direction == "E":
        pos[0] += num
    elif direction == "W":
        pos[0] -= num
    elif direction == "L":
        current_direction = (current_direction - (num // 90)) % 4
    elif direction == "R":
        current_direction = (current_direction + (num // 90)) % 4
    elif direction == "F":
        pos[0] += directions[current_direction][0] * num
        pos[1] += directions[current_direction][1] * num

print(sum(map(abs, pos)))

# --- Part 2 ---

ship = [0, 0]
waypoint = [10, 1]

for instruction in input:
    direction = instruction[0]
    num = int(instruction[1:])

    if direction == "N":
        waypoint[1] += num
    elif direction == "S":
        waypoint[1] -= num
    elif direction == "E":
        waypoint[0] += num
    elif direction == "W":
        waypoint[0] -= num
    elif direction == "L" or direction == "R":
        rotate = 0
        if direction == "L":
            rotate = (num // 90) % 4
        else:
            rotate = (-(num // 90)) % 4

        for i in range(rotate):
            waypoint = [-waypoint[1], waypoint[0]]

    elif direction == "F":
        ship[0] += waypoint[0] * num
        ship[1] += waypoint[1] * num

print(sum(map(abs, ship)))
