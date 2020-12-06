with open("./input.txt") as f:
    lines = [line.strip() for line in f]

# lines = """\
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc""".split("\n")

valid = 0
for line in lines:
    policy, string = line.split(": ")
    rng, letter = policy.split()
    low, high = [int(num) for num in rng.split("-")]
    target = string.count(letter)
    # if low <= target and target <= high:
    #     valid += 1
    try:
        if (string[low-1] == letter) is not (string[high-1] == letter):
            print(f"{letter} in {low} xor {high}: {string}")
            valid += 1
    except:
        pass

print(valid)
