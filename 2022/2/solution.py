input_file_name = 'input'

lines = [l.strip() for l in open(input_file_name) if l]
values = [v.split(' ') for v in lines]


def calculate_score(score_map, round_score_map, values):
    score = 0

    for round in values:
        score += score_map[round[1]]
        score += round_score_map[round[0]][round[1]]

    return score


def part1():
    score_map = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }

    response_score_map = {
        'A': {
            'X': 3,
            'Y': 6,
            'Z': 0,
        },
        'B': {
            'X': 0,
            'Y': 3,
            'Z': 6,
        },
        'C': {
            'X': 6,
            'Y': 0,
            'Z': 3,
        },
    }

    return calculate_score(score_map, response_score_map, values)


def part2():
    score_map = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }

    response_score_map = {
        'A': {
            'X': 3,
            'Y': 1,
            'Z': 2,
        },
        'B': {
            'X': 1,
            'Y': 2,
            'Z': 3,
        },
        'C': {
            'X': 2,
            'Y': 3,
            'Z': 1,
        },
    }

    return calculate_score(score_map, response_score_map, values)


print('Part 1: ', part1())
print('Part 2: ', part2())
