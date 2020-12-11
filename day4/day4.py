from functools import reduce

input = []

with open("input.txt") as f:
    input = f.read().strip().split("\n\n")

input = [x.replace("\n", " ") for x in input]

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
part1 = 0

for passport in input:
    is_valid = True
    for field in fields:
        is_valid = is_valid and field in passport
    
    if is_valid:
        part1 += 1

def check_num(chars, minimum, maximum):
    if not chars.isdigit():
        return False
    
    num = int(chars)
    if num < minimum or num > maximum:
        return False
    
    return True

def check_height(height_string):
    unit = height_string[-2:]

    if unit not in ["cm", "in"]:
        return False
    
    if unit == "cm":
        return check_num(height_string[:-2], 150, 193)
    elif unit == "in":
        return check_num(height_string[:-2], 59, 76)

def check_hair_color(hcl):
    if hcl[0] != "#" or not all(char in "abcdef0123456789" for char in hcl[1:]):
        return False
    
    return True

part2 = 0
for passport in input:
    passport = [x.split(":") for x in passport.split(" ")]
    passport_dict = {}

    for item in passport:
        passport_dict[item[0]] = item[1]

    has_fields = True
    for field in fields:
        if field not in passport_dict:
            has_fields = False
    
    if not has_fields:
        continue

    valid = all([
        check_num(passport_dict["byr"], 1920, 2002),
        check_num(passport_dict["iyr"], 2010, 2020),
        check_num(passport_dict["eyr"], 2020, 2030),
        check_height(passport_dict["hgt"]),
        check_hair_color(passport_dict["hcl"]),
        passport_dict["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        len(passport_dict["pid"]) == 9 and passport_dict["pid"].isdigit()
    ])
    
    if valid:
        part2 += 1
    
print(part1)
print(part2)
