input = []

with open("input.txt") as f:
    input = f.read().strip().split("\n")

input = [int(x) for x in input]

def part1(input):
    for x in input:
        for y in input:
            if x + y == 2020:
                return x*y

def part2(input):
    for x in input:
        for y in input:
            for z in input: 
                if x + y + z == 2020:
                    return x*y*z

print(part1(input))
print(part2(input))
