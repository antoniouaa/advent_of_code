import re

with open("input.txt") as f:
    passports = f.read().split("\n\n")

fields = [
    "cid",
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]

valid = 0
for passport in passports:
    checks = 0
    for field in fields[1:]:
        if field in passport:
            checks += 1
    if checks == 7:
        valid += 1

print(len(passports))
print(valid)

valid = 0
for passport in passports:
    passport = passport.replace("\n", " ")
    if re.search("(?=.*byr:(?:19[2-9][0-9]|200[012]) )(?=.*iyr:(?:201[0-9]|2020) )(?=.*hgt:(?:(?:1[5-8][0-9]|19[0-3])cm|(?:59|6[0-9]|7[0-6])in) )(?=.*hcl:#[0-9a-f]{6} )(?=.*ecl:(?:amb|blu|brn|gry|grn|hzl|oth) )(?=.*pid:[0-9]{9} )(?=.*eyr:(?:202[0-9]|2030) )", passport + " "):
        valid += 1

print(valid)
