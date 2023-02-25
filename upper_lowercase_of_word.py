

def upper_lower(word):
    newword = ''
    for i in range(len(word)):
        if i % 2 == 0:
            newword = newword + word[i].upper()
        else:
            newword = newword + word[i].lower()

    print(newword)


print(upper_lower("ruchirgandhi"))
