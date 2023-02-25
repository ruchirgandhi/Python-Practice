import random


def helper(A, start, end):

    if start >= end:
        return

    randomindex = random.randint(start,end)

    A[randomindex], A[start] = A[start],A[randomindex]

    pivot = A[start]
    orange = start
    green = start

    for green in range(start+1, end+1):

        if A[green] <= pivot:
            orange +=1
            A[orange], A[green] = A[green],A[orange]

    A[orange],A[start] = A[start],A[orange]


    helper(A,0,orange-1)
    helper(A,orange+1,end)

def quicksort(nums):

    helper(nums,0,len(nums)-1)
    return nums


print(quicksort(nums=[3,2,1]))












