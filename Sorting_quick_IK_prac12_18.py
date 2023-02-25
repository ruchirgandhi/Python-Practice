

import random

def quicksort(array):

    def quickhelper(A,start,end):
        if start >= end:
            return
        randomindex = random.randint(start,end)

        A[start],A[randomindex] = A[randomindex],A[start]
        pivot = A[start]

        smaller = start
        bigger = start

        for bigger in range(start+1, end+1):
            if A[bigger] <= pivot:
                smaller +=1
                A[bigger],A[smaller] = A[smaller],A[bigger]

        A[start],A[smaller] = A[smaller],A[start]

        quickhelper(A,start,smaller-1)
        quickhelper(A,smaller+1, end)



    quickhelper(array,0,len(array)-1)
    return array




print(quicksort([15,1,1000000000,458899,10000000,1000000000,45000000]))


