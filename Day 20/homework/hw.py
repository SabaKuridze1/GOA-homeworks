# 1) 1-დან 100-მდე დაითვალეთ ხუთის ჯერადი რიცხვების ჯამი

total_sum = 0


for i in range(1, 101):
    if i % 5 == 0:
        total_sum += i

# შედეგის დაბეჭდვა
print("ხუთის ჯერადი რიცხვების ჯამი:", total_sum)
