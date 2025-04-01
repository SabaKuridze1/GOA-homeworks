def no_space(x):
    final_str = ""
    for char in x:
        if char != " ":
            final_str += char
            
    return final_str