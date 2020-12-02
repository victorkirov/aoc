lines = [l for l in open('input') if l]
values = [int(v) for v in lines]

for value1 in values:
    for value2 in values:
        if 2020 - value1 - value2 in values:
            print(value1 * value2 * (2020 - value1 - value2))
