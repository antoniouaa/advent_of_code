with open("input.txt") as f:
    trees = [line.strip() for line in f.readlines()]

column_width = len(trees[0])

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

product_slopes = 1

for slope in slopes:
    trees_hit = 0
    for i, _ in enumerate(trees):
        down = i * slope[1]
        right = i * slope[0] % column_width
        if down < len(trees):
            if trees[down][right] == "#":
                trees_hit += 1
    product_slopes *= trees_hit

print(product_slopes)
