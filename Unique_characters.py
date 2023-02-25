s = 'abcdefA'

def unique_char(s):

    char = set()

    for i in s:
        if i in char:
            return False
        else:
            char.add(i)
    return True


print(unique_char(s))