input = []

with open("input.txt") as f:
    input = list(map(int, f.read().strip().split("\n")))


part1 = 0
index = 0
for i in range(25, len(input)):
    sums = set([x+y for x in input[i-25:i] for y in input[i-24:i]])
    if input[i] not in sums:
        index = i
        part1 = input[i]
        break

part2 = 0
for i in range(2, index):
    for j in range(0, index-i):
        nums = input[j:j+i]
        if sum(nums) == part1:
            part2 = min(nums) + max(nums)

print(part1)
print(part2)
