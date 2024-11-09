listn=[range(100)]


def minimum(list):
    min_num=(listn[0])
    for i in range(len(listn)):
        if min_num > list[i]:
            min_num = list[i]

    return min_num


result=minimum(1)
print(result)