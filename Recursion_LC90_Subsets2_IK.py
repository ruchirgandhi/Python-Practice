"""
90. Subsets II
Medium

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        results = []
        nums.sort()

        # base case

        def helper(S, i, slate):

            if i == len(S):
                results.append(slate[:])

            else:

                count = 1
                j = i + 1

                while j <= len(S) - 1 and S[j] == S[i]:
                    count += 1
                    j += 1

                for copies in range(0, count + 1):
                    for op in range(copies):
                        slate.append(S[i])
                    helper(S, i + count, slate)
                    for op in range(copies):
                        slate.pop()

        helper(nums, 0, [])

        return results


