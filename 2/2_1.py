lines = [l.strip() for l in open('input') if l]
values_init = [v.split(' ') for v in lines]
values = [[int(v[0].split('-')[0]), int(v[0].split('-')[1]), v[1][0], v[2]] for v in values_init]

valid_count = 0

for value in values:
    min = value[0]
    max = value[1]
    letter = value[2]
    pwd = value[3]

    if min <= pwd.count(letter) <= max:
        valid_count += 1

print(valid_count)
