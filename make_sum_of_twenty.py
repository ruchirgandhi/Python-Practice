"""
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False¶
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False
"""


def sum_twenty(num1, num2):
    if num1 == 20 or num2 == 20 or num1 + num2 == 20:
        return True
    else:
        return False

print(sum_twenty(20,2))

