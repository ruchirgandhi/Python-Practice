
s1 = [1,2,3,4,5,5,6]
s2 = [3,5,6,1,2,4]

from collections import defaultdict

def missing_ele(s1,s2):
    d = defaultdict(int)


    while len(s1)> len(s2):
        for i in s2:
            d[i] +=1


        for i in s1:
            if d[i] == 0:
                return i

            else:
                d[i] -=1

    else:
        for i in s1:
            d[i] +=1


        for i in s2:
            if d[i] == 0:
                return i

            else:
                d[i] -=1



print(missing_ele(s1,s2))

