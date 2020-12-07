# lines
lines = [l.strip() for l in open('input') if l]
values = [int(value) for value in lines[0].split(',')]


def part1(input, noun, verb):
    input = list(input)
    input[1] = noun
    input[2] = verb

    index = 0

    while input[index] != 99:
        if input[index] == 1:
            input[input[index + 3]] = input[input[index + 1]] + input[input[index + 2]]
        elif input[index] == 2:
            input[input[index + 3]] = input[input[index + 1]] * input[input[index + 2]]

        index += 4

    return input[0]


def part2():
    for noun in range(0, 100):
        for verb in range(0, 100):
            if part1(values, noun, verb) == 19690720:
                return 100 * noun + verb


print('Part 1: ', part1(values, 12, 2))
print('Part 2: ', part2())
