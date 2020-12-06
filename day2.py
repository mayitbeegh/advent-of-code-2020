import re
from collections import namedtuple

Password = namedtuple('Password', ['index_1', 'index_2', 'rule_char', 'password'])


def preprocess(raw_input):
    return list(map(lambda x: Password(int(x[1]), int(x[2]), x[3], x[4]),
                    map(lambda x: re.fullmatch(r'([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)', x), raw_input)))


def part_one(passwords):
    return len(list(filter(lambda x: x.index_1 <= x.password.count(x.rule_char) <= x.index_2, passwords)))


def part_two(passwords):
    return len(list(filter(lambda x: (x.index_1 - 1 < len(x.password) and x.password[x.index_1] == x.rule_char) != (
            x.index_2 < len(x.password) and x.password[x.index_2] == x.rule_char), passwords)))


test_inputs = preprocess("""1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".split('\n'))

assert part_one(test_inputs) == 2
assert part_two(test_inputs) == 1

with open('day2.input') as f:
    inputs = preprocess(f.read().splitlines())
    print(part_one(inputs))
    print(part_two(inputs))
