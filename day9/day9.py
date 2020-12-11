import itertools

with open("input.txt") as f:
    numbers = [int(n) for n in f]

start_at = 25

for i, num in enumerate(numbers[start_at:], start=start_at):
    for a, b in itertools.combinations(numbers[i-start_at:i], 2):
        if a + b == num:
            break
    else:
        print(num)
        break


def part2(numbers):
    for i, _ in enumerate(numbers):
        for j, _ in enumerate(numbers[i:], start=i):
            range_ = numbers[i:j+1]
            if sum(range_) == 257342611 and len(range_) > 1:
                print(f"Range: {range_}")
                return range_


proper = part2(numbers=numbers)

print(f"Sum: {sum(proper)}")
print(f"Min: {min(proper)}\nMax: {max(proper)}")
print(min(proper) + max(proper))
