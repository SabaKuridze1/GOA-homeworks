def count_letters_and_digits(s):
    correct = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
    if s == None:
        return 0
    sum = 0
    for i in range(len(s)):
        if s[i] in correct:
            sum += 1
    return sum