from functools import reduce

input = []

with open("input.txt") as f:
    input = f.read().strip().split("\n")


def find_trees(delta):
    trees = 0
    coords = [0, 0]

    while coords[1] < len(input):
        if input[coords[1]][coords[0]] == "#":
            trees += 1
        coords[0] = (coords[0]+delta[0])%len(input[coords[1]])
        coords[1] += delta[1]
    
    return trees

print(find_trees((3, 1)))
print(reduce(lambda x, y: x*y, [find_trees(x) for x in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]))
