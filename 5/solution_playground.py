lines = [l.strip() for l in open('input') if l]
values = [v.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1') for v in lines]


def part1():
    min = None
    max = None

    for value in values:
        row = int(value[:7], 2)
        column = int(value[7:], 2)

        id = row * 8 + column
        max = id if max is None or max < id else max
        min = id if min is None or min > id else min

    return min, max


def part2():
    min, max = part1()
    all_seats = list(range(min, max + 1))

    for value in values:
        row = int(value[:7], 2)
        column = int(value[7:], 2)

        id = row * 8 + column
        all_seats.remove(id)

    return all_seats[0]



print('Part 1: ', part1()[1])
print('Part 2: ', part2())
