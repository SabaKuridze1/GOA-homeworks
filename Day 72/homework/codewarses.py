def multiply(a, b):
    return a * b

def even_or_odd(number):
    if number % 2==0:
        return "Even"
    else:
        return "Odd"
    
def number_to_string(num):
    return str(num)

def solution(string):
    var = ''
    for i in string:
        var = i + var
    return var

def make_negative( number ):
    if number >= 0:
        return (0 - number)
    else:
        return number
    
def opposite(number):
    return -number

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
    
def positive_sum(arr):
    sum = 0 
    for i in arr:
        if i > 0:
            sum += i
    return sum

def repeat_str(repeat, string):
    return string * repeat

def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i * i
    
    return sum

def find_smallest_int(arr):
    mini_num = arr[0]
    for i in arr:
        if i < mini_num :
            mini_num = i
    return mini_num

def string_to_number(s):
    return int(s)

def summation(num):
    for i in range(1, num):
        num += i
        
    return num

def greet():
    return "hello world!"

def count_sheeps(sheep):
    return sheep.count(True)

def no_space(x):
    return x.replace(" ", "")

def double_integer(i):
    return i * 2

def greet(name):
    return "Hello, " + name + " " + "how are you doing today?"

def boolean_to_string(b):
    return str(b)

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
    
def litres(time):
    return time // 2

def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1
    
def maps(a):
    listn = []
    
    for element in a:
        listn.append(element * 2)
        
    return listn

def sum_array(a):
    sum = 0
    for i in a:
        sum += i
    return sum


def sum_array(a):
    sum = 0
    for i in a:
        sum += i
    return sum

def make_upper_case(s):
    return s.upper()