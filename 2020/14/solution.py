from collections import defaultdict

# strings
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]


# parts
def part1():
    memory = defaultdict(int)
    mask = None
    for op in values:
        if op.startswith('mask'):
            mask = op.split('=')[1].strip()
        else:
            mem, value = op.split('=')
            address = int(mem.strip()[4:-1])
            value = int(value)

            value = value | int(mask.replace('X', '0'),2)
            value = value & int(mask.replace('X', '1'),2)

            memory[address] = value

    return sum(memory.values())


def part2():
    memory = defaultdict(int)
    mask = None
    for op in values:
        if op.startswith('mask'):
            mask = op.split('=')[1].strip()
        else:
            mem, value = op.split('=')
            address = int(mem.strip()[4:-1])
            value = int(value)

            address = address | int(mask.replace('X', '0'),2)

            x_count = mask.count('X')

            current_mask = mask.replace('1', 'S')
            current_mask = current_mask.replace('0', 'S')

            for combo in range(int('1'*x_count, 2) + 1):
                bin = "{0:b}".format(combo)
                bin = '0' * (x_count - len(bin)) + bin

                inner_mask = current_mask
                for digit in bin:
                    x_index = inner_mask.index('X')
                    inner_mask = inner_mask[:x_index] + digit + inner_mask[x_index + 1:]

                masked_address = address
                masked_address = masked_address | int(inner_mask.replace('S', '0'),2)
                masked_address = masked_address & int(inner_mask.replace('S', '1'),2)
                memory[masked_address] = value

    return sum(memory.values())


print('Part 1: ', part1())
print('Part 2: ', part2())
