

s1 = ' ruchir is a geek'
'''
def reverse_sentence(s1):

    new_list = []
    spaces = [' ']
    length = len(s1)
    i =0

    while i < length:
        if s1[i] in spaces:
            i +=1
        else:
            new_list.append(s1[i])

        i +=1


'''

def reverse_sentence(s1):
    return ' '.join(reversed(s1.split()))

print(reverse_sentence(s1))