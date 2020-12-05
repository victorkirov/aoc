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
    result = 0

    for value in values:
        row = 0

        current = 64
        for i in range(0,8):
            if value[i] == 'B':
                row += current
            current /= 2

        column = 0
        current = 4
        for i in range(0,3):
            if value[7 + i] == 'R':
                column += current
            current /= 2

        id = row * 8 + column
        result = id if result < id else result

    return result


def part2():
    print(len(values))
    all_seats = []

    for value in values:
        row = 0

        current = 64
        for i in range(0,8):
            if value[i] == 'B':
                row += current
            current /= 2

        column = 0
        current = 4
        for i in range(0,3):
            if value[7 + i] == 'R':
                column += current
            current /= 2

        id = row * 8 + column
        all_seats.append(id)

    all_seats.sort()

    for index in range(0, len(all_seats)):
        if all_seats[index] +1 != all_seats[index + 1]:
            return all_seats[index] + 1



print('Part 1: ', part1())
print('Part 2: ', part2())
