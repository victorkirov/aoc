from collections import defaultdict
from math import ceil

# strings
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]

value_map = {}

for value in values:
    [input, output] = value.split('=>')

    [o_count, o_chem] = output.strip().split(' ')

    i_chems = {}
    for chem in input.split(','):
        [i_count, i_chem] = chem.strip().split(' ')
        i_chems[i_chem] = int(i_count)

    value_map[o_chem] = {
        'count': int(o_count),
        'input': i_chems
    }


def create(chemical, quantity, created, needed):
    if chemical == 'ORE':
        created['ORE'] += quantity
        needed['ORE'] += quantity
        return

    requirements = value_map[chemical]
    reactions = ceil((quantity - (created[chemical] - needed[chemical])) / requirements['count'])

    for i_chem, i_amount in requirements['input'].items():
        create(i_chem, i_amount * reactions, created, needed)

    created[chemical] += requirements['count'] * reactions
    needed[chemical] += quantity


def get_ore_required_for_fuel(amount):
    created = defaultdict(int)
    needed = defaultdict(int)
    create('FUEL', amount, created, needed)
    return created['ORE']


# parts
def part1():
    return get_ore_required_for_fuel(1)


def part2():
    min_ore_for_one_fuel = get_ore_required_for_fuel(1)

    trillion = 1_000_000_000_000
    lower = trillion // min_ore_for_one_fuel
    upper = 2 * lower
    mid = (lower + upper) // 2

    while mid not in [lower, upper]:
        required = get_ore_required_for_fuel(mid)

        if required == trillion:
            break
        if required > trillion:
            upper = mid
        else:
            lower = mid

        mid = (lower + upper) // 2

    return mid

print('Part 1: ', part1())
print('Part 2: ', part2())
