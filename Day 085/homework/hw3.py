def calc(x, y, op):
    if op == "+":
        return f"{x} + {y} = {x + y}"
    elif op == "-":
        return f"{x} - {y} = {x - y}"
    elif op == "*":
        return f"{x} * {y} = {x * y}"
    elif op == "/":
        return f"{x} / {y} = {x / y}"
    

print(calc(2, 3, "+"))