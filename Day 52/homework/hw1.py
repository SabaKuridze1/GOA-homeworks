def get_count(sentence):
    num_vowels = 0
    for i in sentence:
        if i in ['a', 'e', 'i', 'o', 'u']:
            num_vowels += 1
        else:
            pass
    return num_vowels