def hourglass_sum(arr):
    max_sum = -99999
    for row in range(4):
        for col in range(4):
            # arr[row][col] + arr[row][col + 1] + arr[row][col + 2]
            sum_1st_row = sum(arr[row][col:col + 3])
            sum_2nd_row = arr[row + 1][col + 1]
            # arr[row + 2][col] + arr[row + 2][col + 1] + arr[row + 2][col + 2]
            sum_3rd_row = sum(arr[row + 2][col:col + 3])
            total_sum = sum_1st_row + sum_2nd_row + sum_3rd_row

            max_sum = max(total_sum, max_sum)

    return max_sum


array_2d = [[1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]]

result = hourglass_sum(array_2d)
print(result)
