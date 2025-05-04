def disemvowel(string_):
    result = ""
    for i in string_:
        if i not in "aeiouAEIOU":
            result += i
    return result