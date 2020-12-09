from itertools import combinations

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
    lower_bound = 0
    upper_bound = 0

    while True:
        value_list = values[lower_bound:upper_bound]
        list_sum = sum(value_list)

        if list_sum == invalid_number:
            return min(value_list) + max(value_list)
        elif lower_bound > upper_bound - 1:
            upper_bound += 1
        elif list_sum > invalid_number:
            lower_bound += 1
        elif list_sum < invalid_number:
            upper_bound += 1
        else:
            raise RuntimeError(f'{lower_bound}   {upper_bound}')

print('Part 1: ', part1(25))
print('Part 2: ', part2())
