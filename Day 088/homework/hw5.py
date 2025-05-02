def no_vowels(s):
    hide = ""
    vowels = "aeiouAEIOU"
    for i in s:
        if i in vowels:
            hide + "*"
        else:
            hide + i
    return hide


print(no_vowels("sabababassaaaaa"))