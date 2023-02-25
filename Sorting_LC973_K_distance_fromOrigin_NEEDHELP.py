import random

def dist(x):
    return x[0]**2 + x[1]**2

def helper(A,start,end, index):

    if start >= end:
        return
    randomind = random.randint(start, end)
    A[start],A[randomind] = A[randomind],A[start]
    pivot = A[start]
    print("pivot is", pivot)
    orange = start
    green = start

    for green in range(start+1,end+1):
        if A[green] <= pivot:
            orange += 1
            A[green],A[orange] = A[green],A[orange]

    A[start], A[orange] = A[orange],A[start]


    if index < A[orange]:
        helper(A,start,orange-1,index)
    elif index > A[orange]:
        helper(A,orange+1,end,index)
    else:
        return

def kdistance(points):
    lst = [(point, dist(point)) for point in points]
    #print(lst)
    return lst


def test(nums, K):
    lst = kdistance(nums)
    i = 0
    new = []

    for i in range(0,len(lst)):
        curr = lst[i]
        print(curr[1])
        new.append(curr[1])
        i+=1
    print(new)

    helper(new,0,len(new)-1,K)
    return new

print(test([[-3,2],[0,3],[1,4],[0,0]],1))















