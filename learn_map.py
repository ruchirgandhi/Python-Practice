
"""

map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

Syntax :

map(fun, iter)
Parameters :

fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

NOTE : You can pass one or more iterable to the map() function.



Returns :

Returns a list of the results after applying the given function
to each item of a given iterable (list, tuple etc.)

CODE 1



# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()


numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
Output :

[2, 4, 6, 8]


"""

def two(nums):
    return nums**2

list2 = [4,5,6]

print(list(map(two,list2)))


########


def one(nums):
    return [str(n) for n in range(nums)]

list1 = [5,6,7]

print(list((map(one,list1))))