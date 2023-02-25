

import timeit


def one(num):
    list = []
    for n in range(0,num):
        list.append(str(n))

    return list

(one(100000))
print(timeit.timeit())


def two(num):
    return list(map(str,range(num)))


(two(10000000))
print(timeit.timeit())
