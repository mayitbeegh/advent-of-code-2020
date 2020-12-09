from collections import deque
def part_one(inputs, length):
    numbers = list(map(int, inputs))
    preamble = deque(numbers[:length], maxlen=length)
    for number in numbers[length:]:
        if check_valid(preamble, number):
            preamble.append(number)
        else:
            return number
        
def check_valid(preamble, number):
    for i in range(len(preamble)):
        for j in range(i+1, len(preamble)):
            if preamble[i] + preamble[j] == number:
                return True
    return False
        
def part_two(inputs, length):
    numbers = list(map(int, inputs))
    invalid_number = part_one(inputs, length)
    for i in range(len(numbers)):
        for j in range(i+2, len(numbers)):
            if sum(numbers[i:j+1]) == invalid_number:
                return min(numbers[i:j+1]) + max(numbers[i:j+1])
    

test_inputs = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split('\n')

assert part_one(test_inputs, 5) == 127
assert part_two(test_inputs, 5) == 62

with open('day9.input') as f:
    inputs = f.read().splitlines()
    print(part_one(inputs, 25))
    print(part_two(inputs, 25))
