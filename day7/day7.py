input = []

with open("input.txt") as f:
    input = f.read().strip().replace(".", "").replace(" bags", "").replace(" bag", "").split("\n")

input = [x.split(" contain ") for x in input]

bags = {}

for bag in input:
    contains = {}
    for item in bag[1].split(", "):
        if "no other" not in item:
            count = int(item[0])
            contains[item[2:]] = count
    bags[bag[0]] = contains

def contains_shiny_gold(bag):
    if not bags[bag]:
        return False
    if "shiny gold" in bags[bag]:
        return True
    
    has_gold = False
    for key in bags[bag]:
        has_gold |= contains_shiny_gold(key)
    
    return has_gold


part1 = 0
for color in bags:
    if contains_shiny_gold(color):
        part1 += 1


def bags_inside(bag):
    if not bags[bag]:
        return 0

    total = 0
    for item, count in bags[bag].items():
        total += count + count*bags_inside(item)
    
    return total

print(part1)
print(bags_inside('shiny gold'))
