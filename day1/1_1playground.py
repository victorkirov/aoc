lines = [l for l in open('1.in') if l]
values = [int(v) for v in lines]

values.sort()

left_index = 0
right_index = len(values) - 1

sum = values[0] + values[-1]

while sum != 2020:
    left_value = values[left_index]
    right_value = values[right_index]

    if left_value + right_value > 2020:
        right_index -= 1
    elif left_value + right_value < 2020:
        left_index += 1

    sum = values[left_index] + values[right_index]

left_value = values[left_index]
right_value = values[right_index]

print(left_value * right_value)
