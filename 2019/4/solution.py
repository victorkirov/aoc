from collections import defaultdict, Counter

values = list(map(int, open('input').readline().split('-')))


def passes(value, must_have_double):
    counts = defaultdict(lambda: 0)
    prev = None

    for digit in str(value):
        if prev is not None:
            if int(prev) > int(digit):
                return False
        prev = digit
        counts[digit] += 1

    count_counts = dict(Counter(counts.values()))

    if must_have_double:
        return 2 in count_counts

    return max(count_counts.keys()) >= 2


def part1():
    result = 0

    for value in range(values[0], values[1]):
        if passes(value, False):
            result += 1

    return result


def part2():
    result = 0

    for value in range(values[0], values[1]):
        if passes(value, True):
            result += 1

    return result


print('Part 1: ', part1())
print('Part 2: ', part2())
