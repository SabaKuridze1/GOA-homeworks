def sum_array(arr):
    #your code here
    if arr is None or len(arr) == 0:
        return 0
    arr.sort()
    return sum(arr[1:-1])