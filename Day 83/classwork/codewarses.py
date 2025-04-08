def greet():
    return "hello world!"



def make_upper_case(s):
    return s.upper()



def repeat_str(repeat, string):
    return repeat * string



def no_space(x):
    final_str = ""
    for char in x:
        if char != " ":
            final_str += char
            
    return final_str



def create_array(n):
    res = []
    i = 1
    while i <= n: 
        res.append(i)
        i += 1
    return res



def maps(a):
    listn = []
    
    for element in a:
        listn.append(element * 2)
        
    return listn




def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
        


def grader(score):
    if score > 1 or score < 0.6:
        return "F"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    






websites = []
while len(websites) < 1000:
    websites.append("codewars")