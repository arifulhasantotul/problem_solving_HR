def left_rotation(d, arr):
    return arr[d:] + arr[:d]


result = left_rotation(4, [1, 2, 3, 4, 5])

print(result)
