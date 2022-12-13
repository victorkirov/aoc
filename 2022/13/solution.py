from functools import cmp_to_key

input_file_name = 'input'

data = open(input_file_name).read()
values_raw = [v.strip() for v in data.split('\n\n')]
values = [
    [eval(signal) for signal in v.split('\n')]
    for v in values_raw
]
flat_values = [
    eval(signal)
    for v in values_raw
    for signal in v.split('\n')
]


def compare(left, right):
    if not hasattr(left, "__len__") and not hasattr(right, "__len__"):
        if left < right:
            return 1
        if left == right:
            return 0
        return -1

    if not hasattr(left, "__len__"):
        left = [left]
    if not hasattr(right, "__len__"):
        right = [right]

    for i in range(len(left)):
        if i > len(right) - 1:
            return -1

        comp = compare(left[i], right[i])
        if comp != 0:
            return comp

    return 0 if len(right) == len(left) else 1


# parts
def part1():
    result = 0

    for index, value in enumerate(values):
        if compare(value[0], value[1]) == 1:
            print(index)
            result += index + 1

    return result


def part2():
    result = 1
    all_packets = flat_values + [[[2]], [[6]]]

    all_packets.sort(key=cmp_to_key(compare), reverse=True)

    for index, value in enumerate(all_packets):
        print(value)
        if value == [[2]] or value == [[6]]:
            result *= index + 1

    return result

print('Part 1: ', part1())
print('Part 2: ', part2())
