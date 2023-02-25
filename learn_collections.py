from collections import Counter

mylist = [1,2,3,4,5,6,2,2,2,1,1,1,3,4,5,6,]

print(Counter(mylist))

mylist = ["a",'a','b','c','b','d','a']

print(Counter(mylist))

print(Counter("hjsbfhjsfghkb,abfjkghjghsjkgs"))

setenance = "how many times does each chara"

print(Counter(setenance))

setenance = "how many times does each char does many how"

print(setenance.split(" "))

print(Counter(setenance.split(" ")))

c = (Counter(setenance))
print(c.most_common(2))


#################################


from collections import defaultdict

d = {"a":2,"b":3}
print(d)
print(d["a"])

d["correct"] = 20

d = defaultdict(lambda: 100)

print(d["WRONG VALUE"])
print(d)

###############################

mytuple = (10,20,30)
print(mytuple[0])

from collections import namedtuple

DOGS = namedtuple("Dog", ["age","breed","name"])

sammy = DOGS(age=5,breed="huskie",name= "sam")
print(sammy)
print(sammy.age)
print(sammy.breed)
print(sammy.name)

#same AS BELOW

print(sammy[0])
