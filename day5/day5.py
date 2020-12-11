input = []

with open("input.txt") as f:
    input = f.read().strip().split("\n")

def partition(chars, lo, hi):
    for c in chars:
        if c == "F" or c == "L":
            hi = ((hi - lo)//2) + lo
        if c == "B" or c == "R":
            lo = ((hi - lo)//2) + 1 + lo
        
    return lo

ids = set()
part1 = 0
for chars in input:
    row = partition(chars[:-3], 0, 127)
    col = partition(chars[-3:], 0, 7)

    id = (row * 8) + col
    ids.add(id)
    if id > part1:
        part1 = id

part2 = 0
for x in range(part1+1):
    if x not in ids and x+1 in ids and x-1 in ids:
        part2 = x
        break

print(part1)
print(part2)
