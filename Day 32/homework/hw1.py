listn = [1, 2, 3, 4, 234, 1, 333333, 0, 234, 244, 234234]

for i in listn:
    if i > i+1:
        i = i+1

print(i)