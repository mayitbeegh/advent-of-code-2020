def to_seat_id(boarding_pass):
    return int(boarding_pass.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'), 2)


assert to_seat_id('FFFFFFFLLL') == 0
assert to_seat_id('BFFFBBFRRR') == 567
assert to_seat_id('FFFBBBFRRR') == 119
assert to_seat_id('BBFFBBFRLL') == 820


def part_one(inputs):
    return sorted([to_seat_id(boarding_pass) for boarding_pass in inputs])[-1]


def part_two(inputs):
    sorted_seat_ids = sorted([to_seat_id(boarding_pass) for boarding_pass in inputs])
    result = (set(range(sorted_seat_ids[0], sorted_seat_ids[-1] + 1)) - set(sorted_seat_ids)).pop()
    assert result not in sorted_seat_ids
    assert result + 1 in sorted_seat_ids
    assert result - 1 in sorted_seat_ids
    return result


with open('day5.input') as f:
    inputs = f.read().splitlines()
    print(part_one(inputs))
    print(part_two(inputs))
