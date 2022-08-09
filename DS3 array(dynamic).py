def dynamic_array(n, queries):
    seq_list = [[] for i in range(n)]
    last_answer = 0
    result = []

    for q, x, y in queries:
        # query = [1, 0, 5], q=1, x=0, y=5
        idx = (x ^ last_answer) % n
        if q == 1:
            seq_list[idx].append(y)

        else:
            value = y % len(seq_list[idx])
            last_answer = seq_list[idx][value]
            result.append(last_answer)

    return result


output = dynamic_array(2, [[1, 0, 5],
                           [1, 1, 7],
                           [1, 0, 3],
                           [2, 1, 0],
                           [2, 1, 1]])
print(output)
