from itertools import permutations

# strings
lines = [l.strip() for l in open('input') if l]
input_values = [list(v) for v in lines]


# parts
def part1():
    changed = True
    runs = 0

    values = [list(row) for row in input_values]

    while changed:
        runs += 1
        changed = False

        snapshot = [list(row) for row in values]

        for row_index, row in enumerate(snapshot):
            for index, seat in enumerate(row):
                if seat == '.':
                    continue

                taken_counts = 0

                for direction in set(permutations([-1,-1, 1, 0,1], 2)):
                    y = row_index + direction[0]
                    x = index + direction[1]
                    if 0 <= x < len(row) and 0 <= y < len(snapshot):
                        if snapshot[y][x] == '#':
                            taken_counts += 1

                if seat == 'L' and taken_counts == 0:
                    values[row_index][index] = '#'
                    changed = True
                elif seat == '#' and taken_counts >= 4:
                    values[row_index][index] = 'L'
                    changed = True

    return sum([row.count('#') for row in values])


def part2():
    changed = True

    values = [list(row) for row in input_values]

    while changed:
        changed = False

        snapshot = [list(row) for row in values]

        for row_index, row in enumerate(snapshot):
            for index, seat in enumerate(row):
                if seat == '.':
                    continue

                taken_counts = 0

                for direction in set(permutations([-1,-1, 1, 0,1], 2)):
                    distance = 0

                    while True:
                        distance += 1
                        y = row_index + distance * direction[0]
                        x = index + distance * direction[1]

                        if 0 <= x < len(row) and 0 <= y < len(snapshot):
                            if snapshot[y][x] == '#':
                                taken_counts += 1
                                break
                            elif snapshot[y][x] == 'L':
                                break
                        else:
                            break

                if seat == 'L' and taken_counts == 0:
                    values[row_index][index] = '#'
                    changed = True
                elif seat == '#' and taken_counts >= 5:
                    values[row_index][index] = 'L'
                    changed = True

    return sum([row.count('#') for row in values])


print('Part 1: ', part1())
print('Part 2: ', part2())
