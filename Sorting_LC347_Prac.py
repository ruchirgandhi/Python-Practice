
"""
347. Top K Frequent Elements
Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


"""

import random
from collections import Counter

import random
from collections import  Counter

class Solution():

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

    def topKFrequent(self,nums,k):
        Solution.helper(self,nums,0,len(nums)-1, k)
        print(nums)
        result= nums[:k+1]
        print("Result is {}".format(result))
        count = Counter(result)
        print("Count is {}".format(count))
        count = count.most_common(k)
        print("final count is {}".format(count))
        result = []
        for i in range(0,len(count)):
            result.append(count[i][0])
        return result


s = Solution()
print(s.topKFrequent([1,2,2,3,3,4,5,6],4))