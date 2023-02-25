"""

46. Permutations
Medium

5125

122

Add to List

Share
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.


"""



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(S, i, slate):

            if i == len(S):
                result.append(slate[:])
                return

            n = len(S)
            for pick in range(i, n):
                S[pick], S[i] = S[i], S[pick]

                slate.append(S[i])
                helper(S, i + 1, slate)
                slate.pop()
                S[pick], S[i] = S[i], S[pick]

        helper(nums, 0, [])

        return result
