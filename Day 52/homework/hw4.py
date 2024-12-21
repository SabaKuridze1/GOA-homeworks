def find_short(s):
    listn = s.split()
    min = len(listn[0])

    for i in listn:
        if len(i) < min:
            min = len(i)
            
    return min