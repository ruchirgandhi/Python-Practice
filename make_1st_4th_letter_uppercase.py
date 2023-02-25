"""

OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name¶
old_macdonald('macdonald') --> MacDonald
Note: 'macdonald'.capitalize() returns 'Macdonald'


"""

def upper(word):

    newword = ''

    for i in range(len(word)):
        newword = word[0].upper() +word[1:3].lower() + word[3].upper() + word[3:].lower()

    print(newword)

print(upper("RuchirGandhi"))


