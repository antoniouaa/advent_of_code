with open("input.txt") as f:
    instructions = [line.strip() for line in f]


def run_boot(instructions, change):
    acc = 0
    instruction_pointer = 0
    executed = []
    encountered = 0
    while instruction_pointer not in executed and instruction_pointer < len(instructions):
        executed.append(instruction_pointer)
        operation, argument = instructions[instruction_pointer].split()
        if encountered == change:
            operation = "jmp" if operation == "nop" else "nop"
        if operation == "acc":
            acc += int(argument)
            instruction_pointer += 1
        elif operation == "jmp":
            encountered += 1
            instruction_pointer += int(argument)
        else:
            encountered += 1
            instruction_pointer += 1
    else:
        return acc, instruction_pointer


for change, _ in enumerate(instructions):
    acc, i_pointer = run_boot(instructions, change)
    if i_pointer == len(instructions):
        print(acc)
