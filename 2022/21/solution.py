from functools import reduce, cache
from collections import defaultdict
from itertools import product, combinations, permutations

input_file_name = 'input'

lines = [l.strip() for l in open(input_file_name) if l]
values = {
    v.split(':')[0]: v.split(':')[1] for v in lines
}

def part1():
    def parse_val(val):
        cmd = values[val]

        result = ''

        for part in cmd.split(' '):
            if not part:
                continue
            if part in { '+', '-', '*', '/'}:
                result += part
                continue

            try:
                result += str(int(part))
            except ValueError:
                result += f'({parse_val(part)})'

        return result

    return eval(parse_val('root'))


def part2():
    def parse_val(val):
        if val == 'humn':
            return 'humn'

        cmd = values[val]

        result = ''
        left = None
        right = None
        func = None

        for part in cmd.split(' '):
            if not part:
                continue

            if part in { '+', '-', '*', '/'}:
                if val == 'root':
                    func = '=='
                    continue
                func = part
                continue

            try:
                return int(part)
            except ValueError:
                if not left:
                    left = parse_val(part)
                else:
                    right = parse_val(part)

        if type(left) in (int, float) and type(right) in (int, float):
            if func == '+':
                return left + right
            if func == '-':
                return left - right
            if func == '*':
                return left * right
            if func == '/':
                return left / right

        return {
            'left': left,
            'right': right,
            'func': func
        }

    parsed = parse_val('root')

    left = parsed['left']
    right = parsed['right']

    if type(left) == int:
        result = left
        funcs = right
    else:
        result = right
        funcs = left

    while funcs != 'humn':
        left = funcs['left']
        right = funcs['right']
        func = funcs['func']

        if type(left) in (int, float):
            val = left
            funcs = right

            if func == '+':
                result -= val
            if func == '-':
                result -= val
                result *= -1
            if func == '*':
                result /= val
            if func == '/':
                result = val / result
        else:
            val = right
            funcs = left

            if func == '+':
                result -= val
            if func == '-':
                result += val
            if func == '*':
                result /= val
            if func == '/':
                result *= val

    return result


print('Part 1: ', part1())
print('Part 2: ', part2())
