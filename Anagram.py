

def anagram(s1,s2):
    s1= s1.replace(' ','').lower()
    s2 =s2.replace(' ','').lower()
    #return sorted(s1) == sorted(s2)  # this is one way of doing it


#anagram('g1d','dog')

    if len(s1) != len(s2): # quick check
        return False


    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -=1
        else:
            count[letter] =1
    for k in count:
        if count[k] !=0:
            return False

        return True

anagram('d11g','god')

