def human_years_cat_years_dog_years(human_years):
    cat = 0
    dog = 0
    
    if human_years == 1:
        cat = 15
        dog = 15
    elif human_years == 2:
        cat = 24
        dog = 24
        
    else: 
        cat = 4 * (human_years - 2) + 24
        dog = 5 * (human_years - 2) + 24
        
    return [human_years, cat, dog]