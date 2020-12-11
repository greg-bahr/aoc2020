input = []

with open("input.txt") as f:
    input = f.read().strip().split("\n")

input = [x.split(": ") for x in input]

part1 = 0
part2 = 0

for line in input:
    rule = line[0]
    letter = rule.split(" ")[1]
    first = int(rule.split(" ")[0].split("-")[0])
    second = int(rule.split(" ")[0].split("-")[1])

    part1 += first <= line[1].count(letter) <= second
    part2 += (line[1][first-1] == letter) ^ (line[1][second-1] == letter)
        
print(part1)
print(part2)
