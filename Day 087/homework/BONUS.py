def most_frequent_item_count(collection):
    count = 0
    for element in collection:
        if collection.count(element) >= count:
            count = collection.count(element)
    return count