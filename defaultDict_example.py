


#Defaultdict is a container like dictionaries present in the module collections.
# Defaultdict is a sub-class of the dict class that returns a dictionary-like object.
# The functionality of both dictionaries and defualtdict are almost same except for the fact that defualtdict never raises a KeyError.
# It provides a default value for the key that does not exists.




from collections import defaultdict

L = [100,2,3,4,5,6,3,3,1,2,3,4,2,1,4,5,100]

d = defaultdict(int)

print(d)
for i in L:
    d[i] += 1
    print(d)

print(dict(d))

for k,v in d.items():
    print(k,v)