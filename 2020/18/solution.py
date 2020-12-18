import operator

# strings
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]


op_mapping = {
    '+': operator.add,
    '*': operator.mul
}


def evaluate_line(line: str, add_precedence: bool = False):
    left = None
    op = None

    while '(' in line:
        open_index = line.find('(') + 1

        count = 1
        close_index = open_index - 1
        while count != 0:
            close_index += 1
            if line[close_index] == ')':
                count -= 1
            elif line[close_index] == '(':
                count += 1

        line = (
            f'{line[:open_index - 1]}'
            f'{str(evaluate_line(line[open_index: close_index], add_precedence))}'
            f'{line[close_index + 1:]}'
        )

    if add_precedence and '*' in line:
        mul_index = line.find('*')

        left = line[:mul_index]
        right = line[mul_index + 1:]

        line = f'{str(evaluate_line(left, add_precedence))} * {str(evaluate_line(right, add_precedence))}'

    for part in line.split(' '):
        try:
            right = int(part)

            if op:
                left = op_mapping[op](left, right)
                op = None
            else:
                left = right
        except:
            op = part

    return left


# parts
def part1():
    result = 0

    for value in values:
        cur = evaluate_line(value)
        result += cur

    return result


def part2():
    result = 0

    for value in values:
        cur = evaluate_line(value, True)
        result += cur

    return result


print('Part 1: ', part1())
print('Part 2: ', part2())
