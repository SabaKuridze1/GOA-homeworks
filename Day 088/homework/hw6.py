def check_palindrome(word):
    reversed_word = ""

    for char in word:
        char += reversed_word 

    if word == reversed_word:
        return "it's a palindrome"
    else:
        return "it's not a palindrome"
    
print(check_palindrome("saba"))