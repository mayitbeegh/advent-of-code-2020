def part_one(inputs, target_turn):
    previous_dict = {}
    for i_last, last in enumerate(inputs):
        previous_dict[last] = i_last
    i_last += 1
    last = 0
    next_num = 0
    while i_last < target_turn - 1:
        if last in previous_dict:
            next_num = i_last - previous_dict[last]
        else:
            next_num = 0
        previous_dict[last] = i_last
        i_last += 1
        last = next_num
    return next_num


test_inputs = [0, 3, 6]

# print(part_one(test_inputs, 7))
print(part_one([6, 4, 12, 1, 20, 0, 16], 2020))
print(part_one([6, 4, 12, 1, 20, 0, 16], 30000000)) # part two
