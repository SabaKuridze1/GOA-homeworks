def no_vowels(s):
    nonvowels = ""
    for i in s:
        if i not in "aeiou":
            i + nonvowels
    return nonvowels


print(no_vowels("sabababassaaaaa"))
