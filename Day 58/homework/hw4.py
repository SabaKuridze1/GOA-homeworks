def number_of_duplicate_digits(ndigit):
    r = 0
    for i in range(1, ndigit):
        r *= 10
        r += 9 ** i
    return r