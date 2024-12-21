def square_digits(num):
    for i in str(num):
        if str(num)[0] == str(num[0]):
            result = int(i) ** 2
        return result