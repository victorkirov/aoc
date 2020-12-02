lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]

try:
    values = [int(v) for v in values]
except:
    pass

# 1 - complex
# values_init = [v.split(' ') for v in lines]
# values = [[v[0], v[1]] for v in values_init]


def part1():
    result = None

    for value in values:
        print(value)

    return result


def part2():
    pass


print('Part 1: ', part1())
print('Part 2: ', part2())
