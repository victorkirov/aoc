lines = [l.strip() for l in open('input') if l]
values = [v.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1') for v in lines]
ids = [int(value[:7], 2) * 8 + int(value[7:], 2) for value in values]
ids.sort()


def part1():
    return max(ids)


def part2():
    return next(iter(set(range(ids[0], ids[-1])).difference(set(ids))))


print('Part 1: ', part1())
print('Part 2: ', part2())
