def array_manipulation(n, queries):
    # using (n + 2) to avoid error out of boundary
    arr = [0] * (n + 2)

    # perform the query operations
    for a, b, k in queries:
        arr[a] += k  # adding value of k to array index
        arr[b + 1] -= k

    max_num = temp = 0
    for value in arr:
        temp += value
        max_num = max(max_num, temp)

    return max_num


result = array_manipulation(5, [[1, 2, 100],
                                [2, 5, 100],
                                [3, 4, 100]])

print(result)
