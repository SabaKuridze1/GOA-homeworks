def small_enough(array, limit):
    for num in array:
        if num > limit: return False
    return True