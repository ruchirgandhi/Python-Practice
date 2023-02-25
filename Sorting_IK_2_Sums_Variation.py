

target = 7

def two_sum(array):
    d = {}
    for i in range(0,len(array)-1):
        if target - array[i] in d:
            return True
        else:
            d[array[i]] = i
            print(d)
    return False

print(two_sum([5,22,2,3]))

