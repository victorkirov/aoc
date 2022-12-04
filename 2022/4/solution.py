input_file_name = 'input'

lines = [l.strip() for l in open(input_file_name) if l]
values = [v.split(',') for v in lines]

def part1():
    result = 0

    for [elf1, elf2] in values:
        [elf1_min, elf1_max] = [int(v) for v in elf1.split('-')]
        [elf2_min, elf2_max] = [int(v) for v in elf2.split('-')]

        if (
            elf1_min <= elf2_min and
            elf1_max >= elf2_max
            or
            elf2_min <= elf1_min and
            elf2_max >= elf1_max
        ):
            result += 1
    return result


def part2():
    result = 0

    for [elf1, elf2] in values:
        [elf1_min, elf1_max] = [int(v) for v in elf1.split('-')]
        [elf2_min, elf2_max] = [int(v) for v in elf2.split('-')]

        if (
            elf1_min <= elf2_max and
            elf1_max >= elf2_min
            or
            elf2_min <= elf1_max and
            elf2_max >= elf1_min
        ):
            result += 1
    return result


print('Part 1: ', part1())
print('Part 2: ', part2())
