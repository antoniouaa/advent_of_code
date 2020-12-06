with open("./input.txt") as f:
    numbers = [int(num) for num in f]

for i, first in enumerate(numbers):
    for j, second in enumerate(numbers[i:], start=i):
        for third in numbers[j:]:
            if first+second+third == 2020:
                print(first, second, third, first*second*third)
