def duplicate_encode(word):
    word = word.lower()
    result = ""
    for char in word:
        if word.count(char) > 1:
            result += ")"
        else:
            result += "("
            
    return result