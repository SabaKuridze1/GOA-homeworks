def bool_to_word(boolean):
    if boolean == bool("True"):
        return "Yes"
    elif boolean == bool("False"):
        return "No"