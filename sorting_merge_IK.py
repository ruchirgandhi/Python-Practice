def mergesort(A):

    def helper(A,start,end):
        #start= 0
        #end = len(A)-1
        if start >= end:
            return
        mid = (start + end)// 2
        print("mid is {}".format(mid))
        helper(A,start, mid)
        helper(A,mid+1, end)

        i = start
        j = mid +1
        aux = []     #only in merge sort

        while i <= mid and j <= end:
            if A[i] <= A[j]:
                aux.append(A[i])
                print("aux i is {}".format(aux))
                i += 1
            else:
                aux.append(A[j])
                print("aux j is {}".format(aux))
                j += 1

        while i <= mid:
            aux.append(A[i])
            print(A[i])
            i += 1
        while j <= end:
            aux.append(A[j])
            print(A[j])
            j += 1
        A[start:end+1] = aux

    helper(A,0,len(A)-1)

    return A

print(mergesort([9,7,3,4,5,6,1,2]))