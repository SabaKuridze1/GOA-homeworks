def square_root(num):
    for i in range(1, num + 1):
        if num / i == float(i):
            return True
    else:
        return False

print(square_root(16))