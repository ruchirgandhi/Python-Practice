"""
15. 3Sum
Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

"""


nums = [-1,0,1,2,-1,-4]

class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        length = len(nums)

        for i in range(length - 2):  # [8]
            if nums[i] > 0:
                break  # [7]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, length - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:  # [3]
                    l = l + 1
                elif total > 0:  # [4]
                    r = r - 1
                else:  # [5]
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:  # [6]
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:  # [6]
                        r -= 1
                    l += 1
                    r -= 1
        return res

s = Solution()
print(s.threeSum(nums))
