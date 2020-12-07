import re

def part_one(inputs, target_color):
    all_color_rules = {}
    for line in inputs:
        splited = line.split(' bags contain ')
        if 'no other bags.' != splited[-1]:
            color_rules = splited[-1][:-1].split(', ')
            for color_rule in color_rules:
                contained_color = re.fullmatch(r'[0-9]+ (.+) bags*', color_rule)[1]
                if contained_color in all_color_rules:
                    all_color_rules[contained_color].append(splited[0])
                else:
                    all_color_rules[contained_color] = [splited[0]]
    qualified_colors = set()
    add_colors_containing_target_color_to_set(all_color_rules, target_color, qualified_colors)
    return len(qualified_colors)


def add_colors_containing_target_color_to_set(rules, target_color, color_set):
    if target_color in rules:
        color_set.update(rules[target_color])
        for color in rules[target_color]:
            add_colors_containing_target_color_to_set(rules, color, color_set)

        
def part_two(inputs, target_color):
    all_color_rules = {}
    for line in inputs:
        splited = line.split(' bags contain ')
        if 'no other bags.' != splited[-1]:
            all_color_rules[splited[0]] = [(int(pair[1]), pair[2]) for pair in map(lambda x: re.fullmatch(r'([0-9]+) (.+) bags*', x), splited[-1][:-1].split(', '))]
    return count_colors_contained_by(all_color_rules, target_color) - 1 # exclude self

def count_colors_contained_by(rules, target_color):
    if target_color not in rules:
        return 1
    counter = 1 # self
    for count_color_pair in rules[target_color]:
        counter += count_color_pair[0] * count_colors_contained_by(rules, count_color_pair[1])
    return counter

test_inputs = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".split('\n')

test_inputs_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.""".split('\n')

assert part_one(test_inputs, 'shiny gold') == 4
assert part_two(test_inputs_2, 'shiny gold') == 126

with open('day7.input') as f:
    inputs = f.read().splitlines()
    print(part_one(inputs, 'shiny gold'))
    print(part_two(inputs, 'shiny gold'))
