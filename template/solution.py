from functools import reduce

# lines
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]

# groups
data = open('input').read()
values = [v.strip() for v in data.split('\n\n')]
values = [v.split('\n') for v in values]


def part1():
    result = None

    for value in values:
        print(value)

    return result


def part2():
    pass


print('Part 1: ', part1())
print('Part 2: ', part2())
