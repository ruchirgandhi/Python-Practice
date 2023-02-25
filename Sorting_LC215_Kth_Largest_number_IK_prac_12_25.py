### PLEASE LEARN/QUICK SORT FIRST IN ORDER TO ACHIEVE THIS

"""
215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

"""

import random
class Solution():

    def klargest(self,nums,k):
        Solution.helper(self,nums,0,len(nums)-1, len(nums)-k)
        return nums[len(nums)-k]

    def helper(self,A,start,end,index):
        randomindex = random.randint(start,end)
        A[start],A[randomindex] = A[randomindex],A[start]
        pivot = A[start]

        orange= start
        green = start

        for green in range(start+1,end+1):
            if A[green] <= pivot:
                orange += 1
                A[green],A[orange] = A[orange],A[green]

        A[orange],A[start] = A[start],A[orange]

        if index == pivot:
            return
        elif index < pivot:
            Solution.helper(self,A,0,orange-1,index)
        else:
            Solution.helper(self,A, orange+1, end, index)

s= Solution()
print(s.klargest([1,2,3,4,5],2))



















