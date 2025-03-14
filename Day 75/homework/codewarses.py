def bonus_time(salary, bonus):
    if bonus == True:
        return "$" + str(salary * 10)
    else:
        return "$" + str(salary)
    
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

def minimum(arr):
    low = arr[0]
    for each in arr:
        if each < low:
            low = each
    return low
    

def maximum(arr):
    high = arr[0]
    for each in arr:
        if each > high:
            high = each
    return high

def divisible_by(numbers, divisor):
    result = []
    for element in numbers:
        if element % divisor == 0:
            result.append(element)
        else:
            continue
            
    return result