

def is_palindrome(s):
    s_reverse = ""
    for i in range(1, len(s) + 1):
        s_reverse += s[-i]
    if s_reverse.lower() == s.lower():
        return True
    else:
        return False