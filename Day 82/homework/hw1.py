def dont_give_me_five(start,end):
    not_fives = 0
    for i in range(start, end + 1):
        if "5" not in str(i):
            not_fives += 1
    return not_fives