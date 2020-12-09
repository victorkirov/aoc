from itertools import combinations

# lines
lines = [l.strip() for l in open('input') if l]
values = [int(v) for v in lines]


def find_numbers(numbers, value):
    return value in map(sum, combinations(numbers, 2))


def part1(lookback_count):
    for index in range(0, len(values) - lookback_count):
        current_number = values[index + lookback_count]
        if not find_numbers(values[index:index+lookback_count], current_number):
            return current_number


def part2():
    invalid_number = part1(25)

    for index in range(0, len(values)):
        for inner_index in range(index, len(values)):
            value_list = values[index:inner_index]
            if sum(value_list) == invalid_number:
                print(min(value_list) + max(value_list))
                return

print('Part 1: ', part1(25))
print('Part 2: ', part2())
