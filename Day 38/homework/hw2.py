# 2) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვებით სავსე სია შემდეგ კი ამ ფუნქციამ უნდა დააბრუნოს უდიდესი რიცხვი ამ სიიდან

listn=[range(100)]


def maximum(list):
    max_num=(listn[0])
    for i in range(len(listn)):
        if max_num < list[i]:
            max_num = list[i]

    return max_num


result=maximum(1)
print(result)