from math import floor

# lines
lines = [l.strip() for l in open('input') if l]
values = [int(v) for v in lines]


def fuel_fuel(fuel):
    fuel_req = floor(fuel / 3) - 2

    if fuel_req <= 0:
        return 0

    return fuel_req + fuel_fuel(fuel_req)


print('Part 1: ', sum([floor(value / 3) - 2 for value in  values]))
print('Part 2:', sum([fuel_fuel(value) for value in  values]))
