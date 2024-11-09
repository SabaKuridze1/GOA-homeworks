# 8)  დაწერე ფუნქცია, რომელიც იღებს რიცხვს და ამოწმებს, არის თუ არა ის მარტივი რიცხვი.

num = int(input("enter number: "))

def easy(a):
    if num >= 2:
        for i in range(2, a):
            if num % i == 0:
                return "ricxvi"+str(a)+"ar aris martivi"
        return "ricxvi"+str(a)+"aris martivi"
    else:
        return 'ricxvi'+str(a)+'ar aris martivi'
