import itertools
from collections import Counter


file = open("/Users/rucgandh/Downloads/excel-7.txt",'r',encoding='utf-16')

words =file.read().split()


result = (Counter(words).most_common(10))
print(result)

"""
for k,v in result:
    l = ["is",'to','in','on','not','for','the','-','a','due','with','and','after',':','from','of','be','are','as','by','does','up','an',"doesn't",'when','ACI','Leaf','leaf']
    if k in l:
        continue
    else:
        print(k,v)

"""
for k,v in result:

    print(k,v)



