# strings
lines = [l.strip() for l in open('input') if l]
values = [int(v) for v in list(lines[0])]

pattern = [0, 1, 0, -1]


def run_thing(input, input_repetitions, permutations):
    current_permutation = input * input_repetitions
    next_permutation = []

    for _ in range(permutations):
        current_permutation = [0] + current_permutation

        for index, _ in enumerate(current_permutation):
            amount = 0
            pattern_index = 0

            itt_index = 0
            itt_inc = index + 1

            while itt_index < len(current_permutation):
                end_index = min(itt_index + itt_inc, len(current_permutation))
                if pattern[pattern_index] == 0:
                    pass
                elif pattern[pattern_index] == 1:
                    amount += sum(current_permutation[itt_index:end_index])
                elif pattern[pattern_index] == -1:
                    amount -= sum(current_permutation[itt_index:end_index])

                pattern_index += 1
                pattern_index %= len(pattern)
                itt_index += itt_inc

            next_permutation.append(int(str(amount)[-1]))

        current_permutation = next_permutation[:-1]
        next_permutation = []

    return current_permutation[:-1]

# parts
def part1():
    result = run_thing(values, 1, 100)

    return ''.join([str(v) for v in result[:8]])


def part2():
    result = run_thing(values, 10000, 100)

    offset_index = int(''.join(values[:7]))
    return ''.join([str(v) for v in result[offset_index:offset_index + 8]])


print('Part 1: ', part1())  # 25131128
# print('Part 2: ', part2())

# run_thing(values, 1, 1)
