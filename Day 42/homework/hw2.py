def find_smallest_int(arr):
    min_num = arr[0]
    for i in arr:
        if i < min_num :
            min_num = i
    return min_num
