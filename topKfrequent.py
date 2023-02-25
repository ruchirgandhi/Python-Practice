
nums = [1,1,1,1,2,2,2,3,3,4,5]
k =2

from collections import Counter

count= Counter(nums)
print(count)
unique = list(count.keys())
print(unique)

pivot = count[unique[1]]
print(pivot)
