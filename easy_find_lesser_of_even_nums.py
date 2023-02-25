"""


LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd¶
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5

"""

def find_lesser(num1, num2):
    if (num1 % 2 != 1) and (num2 % 2 != 1):
        if num1 > num2:
            print(num2)
        else:
            print(num1)
    else:
        if num1 > num2:
            print(num1)
        else:
            print(num2)

print(find_lesser(13,8))

