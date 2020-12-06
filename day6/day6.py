with open("input.txt") as f:
    inp = f.read()

print(sum(len(set(line.replace("\n", ""))) for line in inp.split("\n\n")))

print(sum(len(set.intersection(*map(set, group.split("\n"))))
          for group in inp.split("\n\n")))
