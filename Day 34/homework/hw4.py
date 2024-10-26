# 4) დაწერე ფუნქცია, რომელიც input()-ით იღებს ორ რიცხვს და ბეჭდავს, რომელია დიდი.

def func():
    num1=int(input("sheiyvanet ricxvi: "))
    num2=int(input("sheiyvanet ricxvi meored: "))
    if num1 > num2:
        print(str(num1) + '>' + str(num2))
    elif num1 < num2:
        print(str(num1) + '<' + str(num2))
    elif num1==num2:
        print(str(num1) + '=' + str(num2))

func()