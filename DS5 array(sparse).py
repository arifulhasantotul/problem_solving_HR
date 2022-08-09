def matching_strings(strings, queries):
    words = {}  # using dictionary to set data as key-value pair
    ans = []
    for word in strings:
        if word in words:
            words[word] += 1  # adding +1 to previous value of the key
        else:
            words[word] = 1  # set value 1 to newly found key

    for q in queries:
        if q in words:
            ans.append(words[q])  # appending key value to new list
        else:
            ans.append(0)

    return ans


result = matching_strings(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab'])
print(result)
