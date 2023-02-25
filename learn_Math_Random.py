import math

#help(math)

value = 4.35

print(math.floor(value))
print(math.ceil(value))

print(round(value))

print(math.pi)

print(math.e)

print(math.log(math.e))

print(math.log(100,10))


## RANDOM


import random

print(random.randint(1,10000))



mylist = list(range(0,20))
print(mylist)

print(random.choice(mylist))

print(random.choices(population=mylist, k=10)) # can pick same numners again

print(random.sample(population=mylist, k=10)) # always pick non-repetative numbers

print(mylist)


