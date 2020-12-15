# strings
lines = [l.strip() for l in open('input2') if l]
values = [int(v) for v in list(lines[0])]

pattern = [0, 1, 0, -1]


def run_thing(input, input_repetitions, permutations):
    current_permutation = input * input_repetitions
    next_permutation = []

    for _ in range(permutations):
        sums = []
        for index, _ in enumerate(current_permutation):
            current_pattern = []
            for entry in pattern:
                current_pattern = current_pattern + ([entry] * (index + 1))

            amount = 0
            for pattern_index in range(len(sums), len(current_permutation)):
                value = current_permutation[pattern_index]

                sums.append(value * current_pattern[(pattern_index + 1 ) % len(current_pattern)])

            amount = sum(sums)
            next_permutation.append(int(str(amount)[-1]))
            print((current_pattern * 10)[1:len(sums) + 1])
            # print(sums)
            # print()
            sums = sums[:index]

        current_permutation = next_permutation
        next_permutation = []

    return current_permutation

# parts
def part1():
    result = run_thing(values, 1, 100)

    return ''.join([str(v) for v in result])[:8]


def part2():
    result = run_thing(values, 10000, 100)

    offset_index = int(''.join(values[:7]))
    return ''.join([str(v) for v in result[offset_index:offset_index + 8]])


# print('Part 1: ', part1())  # 25131128
# print('Part 2: ', part2())

run_thing(values, 1, 1)
