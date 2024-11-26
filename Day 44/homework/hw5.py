def digitize(n):
    number_str = str(n)

    reversed_digits = []
    
    for i in range(len(number_str) - 1, -1, -1):
        digit = int(number_str[i])
        reversed_digits.append(digit)
    
    return reversed_digits