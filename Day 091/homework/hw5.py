def dating_range(age):
    if age <= 14:
        min_age = int(age - 0.10 * age)
        max_age = int(age + 0.10 * age)
    else:
        min_age = int(age / 2 + 7)
        max_age = int(2 * (age - 7))
    return f"{min_age}-{max_age}"