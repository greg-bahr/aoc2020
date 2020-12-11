input = []

with open("input.txt") as f:
    input = f.read().strip().split("\n")

input = [[x, int(y)] for x, y in [x.split(" ") for x in input]]

def part1():
    part1 = 0
    pc = 0
    ran = set()
    while pc not in ran and pc < len(input):
        ran.add(pc)
        instr, arg = input[pc]
        if instr == "acc":
            part1 += arg
            pc += 1
        elif instr == "nop":
            pc += 1
        elif instr == "jmp":
            pc += arg
    
    return (part1, pc >= len(input))

def part2():
    for i in range(len(input)):
        instr, arg = input[i]
        if instr == "acc":
            continue
        
        if instr == "jmp":
            input[i][0] = "nop"
        else:
            input[i][0] = "jmp"

        acc, finished = part1()
        if finished:
            return acc

        input[i][0] = instr
        
print(part1()[0])
print(part2())
