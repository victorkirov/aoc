lines = [l for l in open('1.in') if l]
values = [int(v) for v in lines]


for value in values:
    if 2020 - value in values:
        print((2020 - value) * value)
