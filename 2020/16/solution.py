from collections import defaultdict
from functools import reduce
from math import prod

data = open('input').read()
values = [v.strip() for v in data.split('\n\n')]
values = [v.split('\n') for v in values]

fields = defaultdict(set)
for line in values[0]:
    [name, ranges] = line.split(':')

    for range_item in ranges.split('or'):
        [lower, upper] = range_item.strip().split('-')
        fields[name] |= set(range(int(lower), int(upper) + 1))

my_ticket = [int(v) for v in values[1][1].split(',')]

nearby_tickets = []
for ticket_item in values[2][1:]:
    nearby_tickets.append([int(v) for v in ticket_item.split(',')])

# parts
def part1():
    all_valid_codes = set()

    for field in fields.values():
        all_valid_codes |= field

    error_rate = 0
    valid_tickets = []
    for ticket_item in nearby_tickets:
        invalid_codes = set(ticket_item).difference(all_valid_codes)

        error_rate += sum(invalid_codes)
        if not invalid_codes:
            valid_tickets.append(ticket_item)

    return error_rate, valid_tickets

def part2():
    _, valid_tickets = part1()

    ticket_fields = {i: set(v) for i, v in enumerate(zip(*valid_tickets))}

    field_mapping = {}

    while len(fields) != 0:
        for field, field_values in fields.items():
            rule_positions = []

            for index, ticket_values in ticket_fields.items():
                if not ticket_values.difference(field_values):
                    rule_positions.append(index)

            if len(rule_positions) == 1:
                field_mapping[field] = rule_positions[0]
                fields.pop(field)
                ticket_fields.pop(rule_positions[0])
                break

    req_name = 'departure'

    return prod([my_ticket[i] for f, i in field_mapping.items() if f.startswith(req_name)])


print('Part 1: ', part1()[0])
print('Part 2: ', part2())
