

#args tuple format arbitrary argument


def func(*args):
    return sum(args)

print(func(1,20,30))


#kwargs dictionary format [Key value argument]

def func1(**kwargs):
    print("i would like {} {}".format(kwargs["count"],kwargs["food"]))



print(func1(count = 9,food = "eggs", animal = "Dog" ))


def func2(*args,**kwargs):
    print("I would like to have {} {}".format(args[0], kwargs["food"]))

print(func2(10,20,30,food= "eggs",animal= "cat"))



