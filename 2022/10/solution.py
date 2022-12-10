input_file_name = 'input'

# strings
lines = [l.strip() for l in open(input_file_name) if l]
values = [v.split() for v in lines]


# parts
def part1():
    result = 0

    cycle = 0
    value = 1

    for command in values:
        cycle += 1

        if (cycle - 20) % 40 == 0:
            result += (cycle * value)

        if cycle >= 220:
            break

        if command[0] == 'noop':
            continue

        if command[0] == 'addx':
            cycle += 1

            if (cycle - 20) % 40 == 0:
                result += (cycle * value)

            value += int(command[1])

    return result


def part2():
    result = [[]]

    cycle = 0
    value = 1

    def print_val():
        if (value - 1 <= (cycle - 1) % 40 <= value + 1):
            result[-1].append('#')
        else:
            result[-1].append('.')

        if len(result[-1]) == 40:
            result.append([])

    for command in values:
        cycle += 1

        print_val()

        if command[0] == 'noop':
            continue

        if command[0] == 'addx':
            cycle += 1

            print_val()

            value += int(command[1])

    return '\n' + '\n'.join([''.join(row) for row in result])


print('Part 1: ', part1())
print('Part 2: ', part2())
