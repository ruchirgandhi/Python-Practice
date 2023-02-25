"""

PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

"""

def convert(test):
    newword = ''
    for i in range(0,len(test)):
        newword = newword + test[i]*3

    return newword

print(convert("RUCHIRGANDHI"))