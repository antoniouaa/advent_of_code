with open("input.txt") as f:
    lines = [line.strip() for line in f]

highest = []
for line in lines:
    row, col = line[:-3], line[-3:]
    row = row.replace("B", "1").replace("F", "0")
    col = col.replace("R", "1").replace("L", "0")
    dec_row = int(row, 2)
    dec_col = int(col, 2)
    id_ = dec_row * 8 + dec_col
    highest.append(id_)


highest = sorted(highest)
print(highest[-1])

for i, v in enumerate(highest, start=highest[0]):
    if i != v:
        print(i)
        break
