def arr_check(arr):
    for item in arr:
        if type(item) is not list:
            return False
        else:
            continue
    return True