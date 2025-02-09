def nickname_generator(name):
    vowels = ['a','e','i','o','u']
    if len(name) < 4:
        return 'Error: Name too short'
    if name[2] in vowels:
        return name[:4]
    else:
        return name[:3]