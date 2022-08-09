
def slice_reverse(number):
    """
    list[startIndex:endIndex:startingPosition] => data found from startIndex to lastIndex
    list[::-1]
    if no index is given for startIndex program will select 1st item by default
    if no index is given for endIndex program will select last item by default
    if no index is given for startingPosition program will run from left to right
    if negative index is given for startingPosition program will run from right to left
    """
    return number[::-1]


# result = slice_reverse([1, 2, 3, 4])
def insert_reverse(numbers):
    reverse_list = []
    for num in numbers:
        reverse_list.insert(0, num)

    return reverse_list


result = insert_reverse([1, 2, 3, 4])
