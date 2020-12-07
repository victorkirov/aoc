lines = [l for l in open('input') if l]
values = [int(v) for v in lines]

values.sort()

left_index = 0
right_index = len(values) - 1

upper_bound = right_index
lower_bound = left_index
center_index = (upper_bound - lower_bound) // 2

sum = values[left_index] + values[center_index] + values[right_index]

while sum != 2020:
    left_value = values[left_index]
    center_value = values[center_index]
    right_value = values[right_index]

    sum = left_value + center_value + right_value

    if center_index == upper_bound or center_index == lower_bound:
        if sum > 2020:
            right_index -= 1
            upper_bound = right_index
            lower_bound = left_index
            center_index = (upper_bound - lower_bound) // 2
        elif sum < 2020:
            left_index += 1
            upper_bound = right_index
            lower_bound = left_index
            center_index = (upper_bound - lower_bound) // 2
    else:
        if sum > 2020:
            upper_bound = center_index
            center_index = (lower_bound + center_index) // 2
        elif sum < 2020:
            lower_bound = center_index
            center_index = (upper_bound + center_index) // 2

    sum = left_value + values[center_index] + right_value

left_value = values[left_index]
center_value = values[center_index]
right_value = values[right_index]

print(left_value*center_value*right_value)
