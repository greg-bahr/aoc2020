from collections import defaultdict

input = []

with open("input.txt") as f:
    input = list(map(int, f.read().strip().split("\n")))

adapters = [0, *sorted(input), max(input)+3]
triples = 0
singles = 0
for i in range(1, len(adapters)):
    difference = adapters[i] - adapters[i-1]

    if difference == 1:
        singles += 1
    elif difference == 3:
        triples += 1

print(singles*triples)

compatible = {}
for i in range(len(adapters)):
    adapter = adapters[i]
    compatible[adapter] = []
    for possible in adapters[i+1:i+4]:
        if possible - adapter <= 3:
            compatible[adapter].append(possible)

calculated = defaultdict(int)
def part2(start):
    paths = 0
    for adapter in compatible[start]:
        if adapter == adapters[-1]:
            paths += 1
        elif calculated[adapter] > 0:
            paths += calculated[adapter]
        else:
            paths += part2(adapter)
    
    calculated[start] = paths

    return paths
    

print(part2(0))

