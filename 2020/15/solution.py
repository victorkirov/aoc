data = [l.strip() for l in open('input') if l]
values = [int(v) for v in data[0].split(',')]


def run_for_turns(turn_count):
    index_map = {}
    next_value = None

    runs = len(values)

    for index, value in enumerate(values):
        index_map[value] = index


        next_value = 0 if value not in index_map else index - index_map[value]

    while runs < turn_count - 1:
        value = next_value
        next_value = 0 if next_value not in index_map else runs - index_map[next_value]
        index_map[value] = runs
        runs += 1


    return next_value


def part1():
    return run_for_turns(2020)


def part2():
    return run_for_turns(30000000)


print('Part 1: ', part1())
print('Part 2: ', part2())
