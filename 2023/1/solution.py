input_file_name = 'input'

number_map = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five':  5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

# strings
lines = [l.strip() for l in open(input_file_name) if l]
values = [v for v in lines]

# parts
def part1():
    result = 0

    for value in values:
        left = None
        right = None
        for f in value:
            if f in '1234567890':
                if left is None:
                    left = f
                right = f
        if left is None or right is None:
            raise RuntimeError('FAIL')
        result += int(left + right)

    return result


def part2():
    result = 0

    for value in values:
        init_val = value
        left = None
        right = None

        while len(value) > 0:
            if value[0] in '1234567890':
                left = value[0]
                value = value[1:]
                break

            found = False
            for k, v in number_map.items():
                if value.startswith(k):
                    left = str(v)
                    value = value[len(k):]
                    found = True
                    break

            if found:
                break

            value = value[1:]

        value = init_val
        while len(value) > 0:
            if value[-1] in '1234567890':
                right = value[-1]
                break

            found = False
            for k, v in number_map.items():
                if value.endswith(k):
                    right = str(v)
                    found = True
                    break

            if found:
                break

            value = value[:-1]

        result += int(left + right)

    return result


print('Part 1: ', part1())
print('Part 2: ', part2())
