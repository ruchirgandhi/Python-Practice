

def mergeSort(nums):
    helper(nums, 0, len(nums)-1)
    return nums


def helper(A,start, end):

    if start >= end:
        return

    aux = []

    mid = (start + end) // 2

    helper(A,start,mid)
    helper(A, mid+1, end)

    i = start
    j = mid+1

    while i <= mid and j <= end:
        if A[i] <= A[j]:
            aux.append(A[i])
            i += 1
        else:
            aux.append(A[j])
            j += 1

    while i <= mid:
        aux.append(A[i])
        i =+ 1

    while j <= end:
        aux.append(A[j])
        j +=1


    A[start:end+1]= aux

print(mergeSort([5,4,3]))

