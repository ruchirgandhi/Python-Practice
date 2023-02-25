"""
1213. Intersection of Three Sorted Arrays
Easy

Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.



Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.


"""
def interSection(arr1,arr2,arr3):

    i,j,k,l =0,0,0,0
    result = []
    final = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i =+ 1
            j += 1
        elif arr1[i] > arr2[j]:
            j+=1
        else:
            i +=1

    for k in range(0,len(result)):
        if result[k] not in arr3:
            pass
        else:
            final.append(result[k])


    return final

print(interSection([20,2,3,4,6],[1,20,5,6,7],[1,4,5,6,8,20]))








