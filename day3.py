def part_one(inputs):
    return traverse_slope(inputs, 3, 1)

def part_two(inputs):
    return traverse_slope(inputs, 1, 1) * traverse_slope(inputs, 3, 1) * traverse_slope(inputs, 5, 1) * traverse_slope(inputs, 7, 1) * traverse_slope(inputs, 1, 2)

def traverse_slope(inputs, right, down):
    row = down
    column = right
    path = ''
    while row < len(inputs):
        column %= len(inputs[row])
        path += inputs[row][column]
        row += down
        column += right
    return path.count('#')   

test_inputs = """..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#""".split('\n')
assert part_one(test_inputs) == 7
assert part_two(test_inputs) == 336
with open('day3.input') as f:
    inputs = f.read().splitlines()
    print(part_one(inputs))
    print(part_two(inputs))