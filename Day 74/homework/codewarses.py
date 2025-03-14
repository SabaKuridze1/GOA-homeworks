def area_or_perimeter(l , w):
    if l == w:
        tot = l * w
    else:
        tot = l * 2 + w * 2
    return tot
    

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left >= distance_to_pump / mpg:
        return True
    else:
        return False
    
def enough(cap, on, wait):
    if cap - on >= wait:
        return 0
    else:
        return wait - cap + on  
