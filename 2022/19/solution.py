from functools import cache
from json import dumps, loads

input_file_name = 'input'

lines = [l.strip() for l in open(input_file_name) if l]
blueprints = [
    {
        'index': int(v.split(' ')[1].split(':')[0]),
        'ore_ore_cost': int(v.split(' ')[6]),
        'clay_ore_cost': int(v.split(' ')[12]),
        'obs_ore_cost': int(v.split(' ')[18]),
        'obs_clay_cost': int(v.split(' ')[21]),
        'geo_ore_cost': int(v.split(' ')[27]),
        'geo_obs_cost': int(v.split(' ')[30]),
    }
    for v in lines
]

ORE = 0
CLAY = 1
OBS = 2
GEO = 3

def get_best_geo_count(turns, blueprint_i, robots, resources):
    return get_best_geo_count_(turns, blueprint_i, dumps(robots), dumps(resources))

@cache
def get_best_geo_count_(turns, blueprint_i, robots, resources):
    resources = loads(resources)

    if turns == 0:
        return resources[GEO]

    blueprint = blueprints[blueprint_i]
    robots  = loads(robots)

    max_gen = 0

    next_resources_no_spend = list(map(sum, zip(resources, robots)))

    if resources[ORE] >= blueprint['geo_ore_cost'] and resources[OBS] >= blueprint['geo_obs_cost']:
        next_resources = [*next_resources_no_spend]

        next_resources[ORE] -= blueprint['geo_ore_cost']
        next_resources[OBS] -= blueprint['geo_obs_cost']

        next_robots = [*robots]
        next_robots[GEO] += 1

        max_gen = max(
            get_best_geo_count(turns - 1, blueprint_i, next_robots, next_resources),
            max_gen
        )

        return max_gen

    if (
        resources[ORE] >= blueprint['obs_ore_cost'] and resources[CLAY] >= blueprint['obs_clay_cost']
        and (resources[ORE] - robots[ORE] <= blueprint['obs_ore_cost'] or resources[CLAY] - robots[CLAY] <= blueprint['obs_clay_cost'])
        and robots[OBS] // robots[ORE] < blueprint['geo_obs_cost'] // blueprint['geo_ore_cost']
    ):
        next_resources = [*next_resources_no_spend]

        next_resources[ORE] -= blueprint['obs_ore_cost']
        next_resources[CLAY] -= blueprint['obs_clay_cost']

        next_robots = [*robots]
        next_robots[OBS] += 1

        max_gen = max(
            get_best_geo_count(turns - 1, blueprint_i, next_robots, next_resources),
            max_gen
        )

    if (
        resources[ORE] >= blueprint['clay_ore_cost']
        and resources[ORE] - robots[ORE] <= blueprint['clay_ore_cost']
        and robots[CLAY] // robots[ORE] < blueprint['obs_clay_cost'] // blueprint['obs_ore_cost']
    ):
        next_resources = [*next_resources_no_spend]

        next_resources[ORE] -= blueprint['clay_ore_cost']

        next_robots = [*robots]
        next_robots[CLAY] += 1

        max_gen = max(
            get_best_geo_count(turns - 1, blueprint_i, next_robots, next_resources),
            max_gen
        )

    if (
        resources[ORE] >= blueprint['ore_ore_cost']
        and resources[ORE] - robots[ORE] <= blueprint['ore_ore_cost']
    ):
        next_resources = [*next_resources_no_spend]

        next_resources[ORE] -= blueprint['ore_ore_cost']

        next_robots = [*robots]
        next_robots[ORE] += 1

        max_gen = max(
            get_best_geo_count(turns - 1, blueprint_i, next_robots, next_resources),
            max_gen
        )

    max_gen = max(
        get_best_geo_count(turns - 1, blueprint_i, robots, next_resources_no_spend),
        max_gen
    )

    return max_gen

def part1():
    result = 0

    for blueprint_i, blueprint in enumerate(blueprints):
        robots = [0] * 4
        robots[ORE] = 1
        resources = [0] * 4
        geod_count = get_best_geo_count(24, blueprint_i, robots, resources)

        result += blueprint['index'] * geod_count

    return result


def part2():
    result = 1

    for i in range(3):
        robots = [0] * 4
        robots[ORE] = 1
        resources = [0] * 4
        geod_count = get_best_geo_count(32, i, robots, resources)

        result *= geod_count

    return result


print('Part 1: ', part1())
print('Part 2: ', part2())
