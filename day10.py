from collections import deque
def part_one(inputs):
    numbers = list(sorted(map(int, inputs)))
    numbers = [0] + numbers
    diff_1 = 0
    diff_3 = 1
    for i in range(len(numbers)-1):
        if numbers[i+1] - numbers[i] == 1:
            diff_1 +=1
        elif numbers[i+1] - numbers[i] == 3:
            diff_3 += 1
    return diff_1*diff_3

result = {}


def part_two(inputs):
    numbers = list(sorted(map(int, inputs)))
    numbers = [0] + numbers
    dp = []
    dp.append(0)
    dp.append(1)
    for i in range(2, len(numbers)+1):
        dp.append(0)
        for j in range(1, i):
            if numbers[-j] - numbers[-i] <=3:
                dp[-1]+=dp[j]
    return dp[-1]




def a(l, last_number):
    global result
    counter = 0
    index = 0
    if not l:
        return 1
    while index<len(l) and l[index] - last_number<=3:
        if l[index] in result:
            counter += result[l[index]]
        else:
            d = a(l[index+1:], l[index])
            counter += d

        index+=1

    return counter

test_inputs = """16
10
15
5
1
11
7
19
6
12
4""".split('\n')

test_inputs_2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".split('\n')
assert part_one(test_inputs) == 7*5
assert part_one(test_inputs_2) == 22*10
assert part_two(test_inputs) == 8
assert part_two(test_inputs_2) == 19208

with open('day10.input') as f:
    inputs = f.read().splitlines()
    print(part_one(inputs))
    print(part_two(inputs))
