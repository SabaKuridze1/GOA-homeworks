# 10) დაწერე ფუნქცია, რომელიც იღებს სიას და აბრუნებს მასში მხოლოდ მარტივ რიცხვებს.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_prime_numbers(numbers):
    prime_numbers = []
    for num in numbers:
      if is_prime(num):
        prime_numbers.append(num)
    return prime_numbers