input_file_name = 'input'

values = [l.strip() for l in open(input_file_name) if l]


multiple_map = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2,
}
multiple_rev_map = [
    (-2, '='),
    (-1, '-'),
    (0, '0'),
    (1, '1'),
    (2, '2'),
]


def from_snafu(val):
    result = 0
    digits = list(val)

    multiple = 1

    while digits:
        digit = digits.pop()
        result += multiple_map[digit] * multiple
        multiple *= 5

    return result


def to_snafu(val):
    multiple = 1

    while multiple * 2 < val:
        multiple *= 5

    multiple *= 5

    result_str = ''
    result_str_val = 0

    while multiple > 1:
        multiple /= 5

        for m, s in multiple_rev_map:
            if val <= result_str_val + multiple * m + 2 * multiple / 5:
                result_str += s
                result_str_val += multiple * m
                break

    return result_str


def part1():
    result_sum = 0
    for value in values:
        result_sum += from_snafu(value)

    return to_snafu(result_sum)


print('Part 1: ', part1())
