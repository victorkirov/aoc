lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]

def part1(x_i, y_i):
    result = 0
    x = 0
    y = 0

    while y < len(values) - 1:
        x += x_i
        y += y_i

        row = values[y]
        char = row[x % len(row)]
        if char == '#':
            result += 1

    return result


def part2():
    return part1(1, 1) * part1(3, 1) * part1(5, 1) * part1(7, 1) * part1(1, 2)


print('Part 1: ', part1(3, 1))
print('Part 2: ', part2())
