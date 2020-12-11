input = []

with open("input.txt") as f:
    input = f.read().strip().split("\n\n")

input = [x.split("\n") for x in input]

part1 = 0
for group in input:
    part1 += len(set("".join(group)))

part2 = 0
for group in input:
    questions = set(group[0])
    for test in group[1:]:
        questions &= set(test)
    part2 += len(questions)

print(part1)
print(part2)
