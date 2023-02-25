### PLEASE LEARN/QUICK SORT FIRST IN ORDER TO ACHIEVE THIS

import random
class Solution():
    def findKthLargest(self,Nums,k):
        Solution.helper(Nums, 0, len(Nums)-1, len(Nums)-k)
        return Nums[len(Nums)-k]

    def helper(A, start, end, index):
        if start == end:
            return
        randomindex = random.randint(start, end)

        A[start],A[randomindex] = A[randomindex],A[start]
        pivot = A[start]

        orange = start
        green = start

        for green in range(start+1, end+1):
            if A[green] <= pivot:
                orange += 1
                A[green],A[orange] = A[orange],A[green]

        A[start],A[orange] = A[orange],A[start]

        if index == orange:
            return
        elif index < orange:
            Solution.helper(A,start, orange-1, index)
        else:
            Solution.helper(A, orange+1, end, index)

s= Solution()
print(s.findKthLargest([1,2,3,4,5],2))




