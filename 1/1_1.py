lines = [l for l in open('input') if l]
values = [int(v) for v in lines]


for value in values:
    if 2020 - value in values:
        print((2020 - value) * value)
