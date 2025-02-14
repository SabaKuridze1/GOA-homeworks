def find_multiples(integer, limit):
    new_list = []
    count = integer
    while count <= limit:
        new_list.append(count)
        count += integer
    return new_list