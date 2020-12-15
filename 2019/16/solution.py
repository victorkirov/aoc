# strings
lines = [l.strip() for l in open('input') if l]
values = [int(v) for v in list(lines[0])]

pattern = [0, 1, 0, -1]


def run_thing(input):
    current_permutation = list(input)
    next_permutation = []

    for _ in range(100):
        current_permutation = [0] + current_permutation

        track = []
        for index, _ in enumerate(current_permutation):
            # index = len(current_permutation) - index - 1
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
            track .append(amount)

        current_permutation = next_permutation[:-1]
        next_permutation = []

    return current_permutation[:-1]

# parts
def part1():
    result = run_thing(values)

    return ''.join([str(v) for v in result[:8]])


def part2():
    input = values * 10000

    offset_index = int(''.join(map(str, input[:7])))

    sub_values = input[offset_index:]

    for _ in range(100):
        current_sum = 0
        for i in range(len(sub_values) - 1, -1, -1):
            current_sum += sub_values[i]
            sub_values[i] = current_sum % 10

    return ''.join([str(v) for v in sub_values[:8]])


print('Part 1: ', part1())  # 25131128
print('Part 2: ', part2())
