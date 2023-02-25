"""
78. Subsets

Given an integer array nums, return all possible subsets (the power set).

The solution set must not contain duplicate subsets.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        results = []

        def helper(S, i, slate):

            # basecase
            if i == len(S):

                results.append(slate[:])
                return
            else:

                # exclude
                helper(S, i + 1, slate)

                # include
                slate.append(S[i])
                helper(S, i + 1, slate)
                slate.pop()

        helper(nums, 0, [])
        return results
