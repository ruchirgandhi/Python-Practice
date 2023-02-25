nums = [-2,1,-3,4,-1,2,1,-5,4]

class Solution:
    def LargestSum(self, nums):
        for i in range(1,len(nums)):
            if nums[i-1] >0:
                nums[i] = nums[i] + nums[i-1]
                print(nums)
        return max(nums)

s = Solution()
print(s.LargestSum(nums))