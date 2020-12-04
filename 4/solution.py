import re
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]


def part1():
    result = 0

    required_fields = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
    current_fields = set(required_fields)

    for value in values + ['']:
        if value:
            line_fields = set(re.findall(f'({"|".join(required_fields)}):', value))
            current_fields = current_fields - line_fields
        else:
            if len(current_fields) == 0:
                result += 1
            current_fields=set(required_fields)

    return result


def part2():
    validations = [
        '(byr)?:((19[2-9][0-9])|(200[0-2]))\s',
        '(iyr)?:((201[0-9]|2020))\s',
        '(eyr)?:((202[0-9]|2030))\s',
        '(hgt)?:(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))\s',
        '(hcl)?:(#[0-9a-fA-F]{6})\s',
        '(ecl)?:(amb|blu|brn|gry|grn|hzl|oth)\s',
        '(pid)?:([0-9]{9})\s',
    ]

    result = 0

    required_fields = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
    current_fields = set(required_fields)

    for value in values + ['']:
        if value:
            for regex in validations:
                v_line_fields = re.findall(regex, f'{value} ')
                line_fields = set([field[0] for field in v_line_fields if field[0]])
                current_fields = current_fields - line_fields
        else:
            if len(current_fields) == 0:
                result += 1
            current_fields=set(required_fields)

    return result


print('Part 1: ', part1())
print('Part 2: ', part2())
