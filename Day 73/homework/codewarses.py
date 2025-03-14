def check_exam(arr1, arr2):
    score = 0

    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            score = score + 4
        elif arr2[i] != "":
            score -= 1
    return max(score, 0)

def sum_str(a, b):
    if a == "":
        copy_a = 0
    else:
        copy_a = int(a)
        
    if b == "":
        copy_b = 0
    else:
        copy_b = int(b)
            
            
    result = copy_a + copy_b
    final_result = str(result)
    
    return final_result

def cookie(x):
    if type(x) == type('x'):
        name = "Zach"
    elif type(x) == type(42) or type(x) == type(3.14):
        name = "Monica"
    else:
        name = "the dog"
        
    return "Who ate the last cookie? It was " + name + "!"

def pythagorean_triple(integers):
    integers.sort()
    if integers[2] ** 2 == integers[0] ** 2 + integers[1] ** 2:
        return True
    else:
        return False
    
def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    elif age >= 21:
        return "drink whisky"
    
def no_space(x):
    return x.replace(" ", "")
