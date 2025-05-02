def string_clean(s):
    result = ""
    for elem in s:
        if elem not in "1234567890":
            result += elem
    return result
