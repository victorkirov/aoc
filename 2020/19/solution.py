# groups
data = open('input').read()
values = [v.strip() for v in data.split('\n\n')]
values = [v.split('\n') for v in values]

rules = {int(r.split(':')[0]): [list(n.strip().strip('"').split(' ')) for n in r.split(':')[1].split('|')] for r in values[0]}
inputs = values[1]


def match_rule(val, rule):
    if not val:
        return ''

    inner_rules = rules[rule]

    if len(inner_rules) == 1:
        try:
            int(inner_rules[0][0])
        except:
            if val[0] == inner_rules[0][0]:
                return [val[0]]
            return []

    matches = []
    for sub_rule in inner_rules:
        inner_matches = {''}

        for rule in map(int, sub_rule):
            new_inner_matches = set()
            for inner_match in inner_matches:
                rule_matches = match_rule(val[len(inner_match):], rule)

                for rule_match in rule_matches:
                    new_inner_matches.add(inner_match + rule_match)

            if not new_inner_matches:
                inner_matches = {''}
                break
            inner_matches = new_inner_matches

        if list(inner_matches)[0] != '':
            matches.extend(inner_matches)

    return list(set(matches))


def find_match_count():
    result = 0

    for value in inputs:
        matches = match_rule(value, 0)
        if value in matches:
            result += 1

    return result


print('Part 1: ', find_match_count())

rules[8] = [[42], [42, 8]]
rules [11] = [[42, 31], [42, 11, 31]]

print('Part 2: ', find_match_count())
