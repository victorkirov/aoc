lines = [l for l in open('input') if l]
values = [int(v) for v in lines]


def part1():
    for value in values:
        if 2020 - value in values:
            return ((2020 - value) * value)


def part2():
    for value1 in values:
        for value2 in values:
            if 2020 - value1 - value2 in values:
                 return (value1 * value2 * (2020 - value1 - value2))


print('Part 1: ', part1())
print('Part 2: ', part2())
