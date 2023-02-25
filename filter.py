"""

filter function
The filter function returns an iterator yielding those items of iterable for which function(item) is true. Meaning you need to filter by a function that returns either True or False. Then passing that into filter (along with your iterable) and you will get back only the results that would return True when passed to the function.
"""


def even(nums):
    return nums % 2 == 0

nums = [1,2,3,4,54,5,56,6,76,7,78,8,8,8,7,5,5,3,1,2]

print(list(filter(even, nums)))


