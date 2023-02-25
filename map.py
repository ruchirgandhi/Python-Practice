## MAP function

"""
def square(nums):
    return nums**2

mylist = [1,2,3,4,5]


print(list(map(square,mylist)))


"""


def splicer(myWords):
    if len(myWords) % 2 == 0:
        return "even"
    else:
        return myWords[0]

myWords = ['John','Cindy','Sarah','Kelly','Mike']

print(list(map(splicer, myWords)))