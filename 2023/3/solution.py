input_file_name = 'input'

# strings
lines = [l.strip() for l in open(input_file_name) if l]
values = [list(v) for v in lines]


def has_sign_neighbour(xC, yC, sign=None):
    for x in range(xC - 1, xC + 2):
        for y in range(yC - 1, yC + 2):
            if x == xC and y == yC:
                continue

            if x < 0 or y < 0 or x >= len(values[0]) or y >= len(values):
                continue

            if sign:
                if values[y][x] == sign:
                    return f'{x},{y}'
            elif values[y][x] not in list('.1234567890'):
                return True

    return False


# parts
def part1():
    result = 0

    for y in range(len(values)):
        value = values[y]
        current = ''
        is_part = False

        for x in range(len(value)):
            c = value[x]

            if c not in list('1234567890'):
                if current and is_part:
                    result += int(current)

                current = ''
                is_part = False
            else:
                current += c

                if is_part or has_sign_neighbour(x, y):
                    is_part = True

        if current and is_part:
            result += int(current)

    return result


def part2():
    stars = {}

    for y in range(len(values)):
        value = values[y]
        current = ''
        is_part = False

        for x in range(len(value)):
            c = value[x]

            if c not in list('1234567890'):
                if current and is_part:
                    if is_part not in stars:
                        stars[is_part] = [int(current)]
                    else:
                        stars[is_part].append(int(current))

                current = ''
                is_part = False
            else:
                current += c

                if not is_part:
                    is_part = has_sign_neighbour(x, y, '*')

        if current and is_part:
            if is_part not in stars:
                stars[is_part] = [int(current)]
            else:
                stars[is_part].append(int(current))

    return sum([s[0] * s[1] for s in stars.values() if len(s) ==2])


print('Part 1: ', part1())
print('Part 2: ', part2())
