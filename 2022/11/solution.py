from functools import cache
from math import lcm

input_file_name = 'input'

data = open(input_file_name).read()


def part1():
    monkeys = [v.strip() for v in data.split('\n\n')]
    monkeys = [
        {
            "inspected": 0,
            "test": int((vals:=v.split('\n'))[3].split(' ')[-1]),
            "op": ' '.join(vals[2].strip().split(' ')[3:]),
            "items": [
                int(i.replace(',', ''))
                for i in (vals[1].strip()).split(' ')[2:]
            ],
            'pass': int(vals[4].split(' ')[-1]),
            'fail': int(vals[5].split(' ')[-1]),
        }
        for v in monkeys
    ]

    for _ in range(20):
        for monkey in monkeys:
            while len(monkey["items"]) > 0:
                monkey["inspected"] += 1
                old = monkey["items"].pop(0)
                new = eval(monkey['op'])

                item = new //3

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


def part2():
    monkeys = [v.strip() for v in data.split('\n\n')]
    monkeys = [
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
        for v in monkeys
    ]

    lcm_val = lcm(*[monkey['test'] for monkey in monkeys])

    @cache
    def throw(start_monkey, val):
        throws = { i: 0 for i in range(len(monkeys)) }
        throws[start_monkey] = 1

        monkey = monkeys[start_monkey]

        old = val
        new = eval(monkey['op'])

        new_val = new % lcm_val

        if new_val % monkey['test'] == 0:
            next_monkey = monkey["pass"]
        else:
            next_monkey = monkey["fail"]

        if next_monkey < start_monkey:
            return next_monkey, new_val, throws

        final_monkey, final_val, other_throws = throw(next_monkey, new_val)

        for monkey_num, other_throw in other_throws.items():
            throws[monkey_num] += other_throw
        return final_monkey, final_val, throws

    inspect_count = { i: 0 for i in range(len(monkeys)) }

    for _ in range(10000):
        for monkey_num, monkey in enumerate(monkeys):
            while len(monkey["items"]) > 0:
                item_val = monkey["items"].pop()

                final_monkey, final_val, throws = throw(monkey_num, item_val)

                for monkey_i, throw_val in throws.items():
                    inspect_count[monkey_i] += throw_val

                monkeys[final_monkey]['next_items'].append(final_val)
        for monkey in monkeys:
            monkey['items'] = monkey['next_items']
            monkey['next_items'] = []

    print(inspect_count)

    counts = list(inspect_count.values())
    counts.sort(reverse=True)


    return counts[0] * counts[1]



print('Part 1: ', part1())
print('Part 2: ', part2())
