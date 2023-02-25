

"""
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd¶
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5

def lesser_of_two_events(a,b):
    if a%2 ==0 and b%2 ==0:
        if a<b:
            return a
        else:
            return b
    else:
        if a<b:
            return b
        else:
            return a


print(lesser_of_two_events(9,4))


"""

"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False


def animal_crackers(text):
    ans = (text.split(" "))
    if ans[0][0] == ans[1][0]:
        return True
    else:
        return False

print(animal_crackers("Ruchir Gandhi"))
"""
"""

MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False


def makes_twenty(a,b):
    if a==20 or b ==20 or a+b == 20:
        return True
    else:
        return False

print(makes_twenty(10,1))

"""
"""
# LEVEL 1 problems
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name¶
old_macdonald('macdonald') --> MacDonald
Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_mcdonald(name):
    res = []

    for i in range(len(name)):
        if i ==0:
            res.append(name[i].upper())
        elif i ==3:
            res.append(name[i].upper())
        else:
            res.append(name[i])


    return "".join(res)


print(old_mcdonald("mcdonanlds"))

"""

"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

>>> "--".join(['a','b','c'])
>>> 'a--b--c'
This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

>>> " ".join(['Hello','world'])
>>> "Hello world"

def master_yoda(name):
    res = name.split(" ")
    res.reverse()
    return " ".join(res)


print(master_yoda("Ruchir is a nice person"))


"""


"""
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True
NOTE: abs(num) returns the absolute value of a number


def almost_there(num):
    if abs(num - 100) <= 10 or abs(100 - num) <= 10:
        return True
    elif abs(num - 200) <= 10 or abs(200 - num) <= 10:
        return True
    else:
        return False

print(almost_there(211))
"""
"""
LEVEL 2 PROBLEMS
FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False



def has_33(list):
    for i in range(len(list)-1):
        if list[i] ==3 and list[i+1] ==3:
            return True
    else:
        return False

print(has_33([3,1,3,3]))

"""
"""
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


def myfunc(text):
    res = []
    for i in range(len(text)):
        res.append(text[i]*3)

    return "".join(res)

print(myfunc("missisippi"))
"""

"""
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'¶
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19

"""

def backjack(a,b,c):


    sum = a+b+c
    if sum <= 21:
        return sum

    elif sum >21 and (a|b |c) ==11:
        sum = sum-10
        if sum > 21:
            return "BUST"
        else:
            return sum
    else:
        return sum

print(backjack(11,0,11))