from functools import reduce

input_file_name = 'input'

lines = [l.strip() for l in open(input_file_name) if l]
values = [v for v in lines]

bag_balls = {
    'red': 12,
    'green': 13,
    'blue': 14
}

# parts
def part1():
    result = 0

    for value in values:
        [game, outcomes] = value.split(':')
        id = int(game.split(' ')[1])

        valid = True
        for outcome in outcomes.split(';'):
            colours = outcome.split(',')

            for colour in colours:
                [cnt, name] = colour.strip().split(' ')
                if bag_balls[name] < int(cnt):
                    valid = False
                    break

            if not valid:
                break

        if valid:
            result += id

    return result


def part2():
    result = 0

    for value in values:
        [game, outcomes] = value.split(':')
        id = int(game.split(' ')[1])

        counts = {}
        for outcome in outcomes.split(';'):
            colours = outcome.split(',')

            for colour in colours:
                [cnt, name] = colour.strip().split(' ')
                if name not in counts:
                    counts[name] = 0
                counts[name] = max(int(cnt), counts[name])

        result += reduce(lambda a, b: a * b, counts.values())

    return result


print('Part 1: ', part1())
print('Part 2: ', part2())
