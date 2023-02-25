def mergesort(array):

    def helper(A,start,end):

        if start >= end:
            return
        mid = (start + end) //2

        helper(A,start, mid)
        helper(A,mid+1,end)

        i = start
        j = mid +1

        aux = []

        while i <= mid and j <= end:
            if A[i] <= A[j]:
                aux.append(A[i])
                i += 1
            else:
                aux.append(A[j])
                j += 1
        while i <= mid:
            aux.append(A[i])
            i += 1
        while j <= end:
            aux.append(A[j])
            j += 1

        A[start:end+1] = aux
    helper(array,0,len(array)-1)
    return array

print(mergesort([3,2,1,4,5,6,20]))

