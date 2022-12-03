input_file_name = 'input'

lines = [l.strip() for l in open(input_file_name) if l]
values = [v for v in lines]

def get_score(char):
    return ord(char) - 65 + 27 if ord(char) < 97 else ord(char) - 97 + 1

def part1():
    result = 0

    for value in values:
        lng = len(value)
        left = set(value[:lng//2])
        right = set(value[lng//2:])

        char = left.intersection(right).pop()
        result += get_score(char)

    return result


def part2():
    result = 0

    for i in range(0, len(values), 3):
        first = set(values[i])
        second = set(values[i + 1])
        third = set(values[i + 2])

        char = first.intersection(second).intersection(third)
        result += get_score(char)

    return result


print('Part 1: ', part1())
print('Part 2: ', part2())
