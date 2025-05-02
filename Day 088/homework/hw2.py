def divide_digits(number):
  sum = 0
  num_str = str(number)
  for digit in num_str:
    sum += int(digit)
  return number / sum

print(divide_digits(12))