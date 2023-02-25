string = "abcabcdefghijkl"

list = [1,2,3,4,5,6,7,8,8,8,6,7,4,6,2,1]


from collections import Counter

max = Counter(list).most_common(1)
for key,val in max:
    print("maximum occurance of the number {} in list is {} times".format(key,val))

str = Counter(string).most_common(1)
for key,val in str:
    print("maximum occurance of the letter {} in string is {} times".format(key,val))
