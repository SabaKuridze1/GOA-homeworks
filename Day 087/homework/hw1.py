def get_drink_by_profession(param):
    new_param = param.lower()
    
    if new_param == 'jabroni':
        return 'Patron Tequila'
    elif new_param == 'school counselor':
        return 'Anything with Alcohol'
    elif new_param == 'programmer':
        return 'Hipster Craft Beer'
    elif new_param == 'bike gang member':
        return "Moonshine"
    elif new_param == 'politician':
        return "Your tax dollars"
    elif new_param == "rapper":
        return "Cristal"
    else:
        return "Beer"