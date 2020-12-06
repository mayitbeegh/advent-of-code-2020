def part_one(inputs):
    numbers = list(map(int, inputs))
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == 2020:
                return numbers[i] * numbers[j]


def part_two(inputs):
    numbers = list(map(int, inputs))
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            for k in range(j, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    return numbers[i] * numbers[j] * numbers[k]


test_inputs = """1721
979
366
299
675
1456""".split('\n')

assert part_one(test_inputs) == 514579
assert part_two(test_inputs) == 241861950

with open('day1.input') as f:
    inputs = f.read().splitlines()
    print(part_one(inputs))
    print(part_two(inputs))
