from functools import reduce

def part_one(inputs):
    # {'a', 'ab'} -> {'a'} U {'a', 'b'} -> {'a', 'b'} -> 2
    return sum(map(lambda x: len(set.union(*map(set, x))), inputs))

def part_two(inputs):
    return sum(map(lambda x: len(set.intersection(*map(set, x))), inputs))

def preprocess(raw_input):
    return [[f for f in t.split()] for t in raw_input.split('\n\n')]

test_inputs = preprocess("""abc

a
b
c

ab
ac

a
a
a
a

b""")

assert part_one(test_inputs) == 11
assert part_two(test_inputs) == 6

with open('day6.input') as f:
    inputs = preprocess(f.read())
    print(part_one(inputs))
    print(part_two(inputs))
