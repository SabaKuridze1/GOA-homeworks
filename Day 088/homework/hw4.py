def most_repeated_number(nums):
    most_common = None
    highest_count = 0

    for num in nums:
        count = nums.count(num)
        if count > highest_count:
            highest_count = count
            most_common = num

    return most_common

print(most_repeated_number([1, 1, 1, 1, 2, 13, 2, 1]))