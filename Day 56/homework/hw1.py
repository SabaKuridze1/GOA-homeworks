def to_jaden_case(string):
    words = string.split()

    jaden_cased_words = []

    for word in words:
        if word.lower() == "Aren't":
            jaden_cased_words.append(word)
        else:
            jaden_cased_words.append(word.capitalize())

    return ' '.join(jaden_cased_words)