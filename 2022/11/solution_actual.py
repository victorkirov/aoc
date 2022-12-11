from copy import deepcopy
from math import lcm

input_file_name = 'input'

data = open(input_file_name).read()

rows = [v.strip() for v in data.split('\n\n')]
monkeys_raw = [
    {
        "inspected": 0,
        "test": int((vals:=v.split('\n'))[3].split(' ')[-1]),
        "op": ' '.join(vals[2].strip().split(' ')[3:]),
        "items": [
            int(i.replace(',', ''))
            for i in (vals[1].strip()).split(' ')[2:]
        ],
        "next_items": [],
        'pass': int(vals[4].split(' ')[-1]),
        'fail': int(vals[5].split(' ')[-1]),
    }
    for v in rows
]

lcm_val = lcm(*[monkey['test'] for monkey in monkeys_raw])


def part(rounds, simplify_func):
    monkeys = deepcopy(monkeys_raw)

    for _ in range(rounds):
        for monkey in monkeys:
            while len(monkey["items"]) > 0:
                monkey["inspected"] += 1
                old = monkey["items"].pop(0)
                new = eval(monkey['op'])

                item = simplify_func(new)

                if item % monkey['test'] == 0:
                    monkeys[monkey["pass"]]["items"].append(item)
                else:
                    monkeys[monkey["fail"]]["items"].append(item)

    inspect_count = [
        monkey["inspected"]
        for monkey in monkeys
    ]

    inspect_count.sort(reverse=True)

    return inspect_count[0] * inspect_count[1]



print('Part 1: ', part(20, lambda x: x // 3))
print('Part 2: ', part(10000, lambda x: x % lcm_val))
