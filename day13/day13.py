from functools import reduce

input = []

with open("input.txt") as f:
    input = f.read().strip().split("\n")
    input[1] = input[1].split(",")

timestamp = int(input[0])
bus_ids = [int(x) for x in input[1] if x.isdigit()]

lowest = 9999999999
best_id = 0
for id in bus_ids:
    extra_wait = id - (timestamp % id)

    if extra_wait < lowest:
        lowest = extra_wait
        best_id = id

print(best_id*lowest)

schedule = {}
for i in range(len(input[1])):
    if input[1][i] != "x":
        schedule[int(input[1][i])] = i

timestamp = 0
N = reduce(lambda x, y: x*y, schedule.keys())

for bus, t in schedule.items():
    n = N // bus
    b = bus - t
    x = 1
    while n * x % bus != 1:
        x += 1
    timestamp += n * b * x

print(timestamp % N)

