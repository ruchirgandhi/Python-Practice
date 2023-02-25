
'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
'''



class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        cur_num = max_num = nums[0]

        for i in range(1, length):
            cur_num = max(nums[i], cur_num + nums[i])
            max_num = max(cur_num, max_num)

        return max_num

s = Solution()
new = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(new)