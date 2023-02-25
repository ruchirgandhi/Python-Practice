
from collections import Counter

list = [0,1,2,0,1,0,2,3,0,4,5,6]


count = list.count(0)
print(count)

for i in list:
    list.remove(0)
    list.append(0)

print(list)

