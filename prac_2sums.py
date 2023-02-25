nums = [2,7,11,15]
target = 9

class Solution:
    def twosum(self, nums, target):

        dict = {}

        for i,num in enumerate(nums):
            if (target-num) in dict:
                return [target- num],i
            dict[num] = i


s = Solution()
print(s.twosum(nums,target))