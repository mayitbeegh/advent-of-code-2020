def part_one(inputs):
    return get_acc(inputs, False)

        
def part_two(inputs):
    for current_line in range(len(inputs)):
        backup = inputs[current_line]
        try:
            if inputs[current_line][:3] == 'nop' and inputs[current_line][4:] != '+0':
                inputs[current_line] = 'jmp' + inputs[current_line][3:]
                return get_acc(inputs, True)
            elif inputs[current_line][:3] == 'jmp':
                inputs[current_line] = 'nop' + inputs[current_line][3:]
                return get_acc(inputs, True)
        except:
            inputs[current_line] = backup
        

def get_acc(inputs, raise_on_loop):
    executed_lines = set()
    acc = 0
    current_line = 0
    while current_line not in executed_lines:
        if current_line >= len(inputs):
            return acc
        executed_lines.add(current_line)
        if inputs[current_line][:3] == 'nop':
            current_line += 1
        elif inputs[current_line][:3] == 'jmp':
            current_line += int(inputs[current_line][4:])
        elif inputs[current_line][:3] == 'acc':
            acc += int(inputs[current_line][4:])
            current_line += 1
    if raise_on_loop:
        raise
    else:
        return acc

test_inputs = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".split('\n')

assert part_one(test_inputs) == 5
assert part_two(test_inputs) == 8

with open('day8.input') as f:
    inputs = f.read().splitlines()
    print(part_one(inputs))
    print(part_two(inputs))
