from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

# strings
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]


# parts
def part1():
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }

    result = 0

    def process_line(value):
        found_brackets = []
        for bracket in list(value):
            if bracket not in pairs:
                found_brackets.append(bracket)
            else:
                previous_open_bracket = found_brackets.pop()
                if previous_open_bracket != pairs[bracket]:
                    return points[bracket]
        return 0

    for value in values:
        result +=  process_line(value)

    return result


def part2():
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }

    closing_pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }

    scores = []

    def process_line(value):
        found_brackets = []
        for bracket in list(value):
            if bracket not in closing_pairs:
                found_brackets.append(bracket)
            else:
                previous_open_bracket = found_brackets.pop()
                if previous_open_bracket != closing_pairs[bracket]:
                    return 0

        score = 0

        found_brackets.reverse()

        for bracket in found_brackets:
            score *= 5
            score += points[pairs[bracket]]

        return score

    for value in values:
        score =  process_line(value)
        if score != 0:
            scores.append(score)

    scores.sort()
    return scores[int((len(scores) - 1) / 2)]


print('Part 1: ', part1())
print('Part 2: ', part2())
