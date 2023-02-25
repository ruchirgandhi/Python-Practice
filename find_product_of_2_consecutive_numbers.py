
# Given an array, find the largest product of two  elements.



class Solution:
    def maxProd(self,nums):
        ans = max(nums[-1] * nums[-2], nums[0] * nums[1])
        return ans

if __name__ == "__main__":
    nums = [1, 2, -6, 3, -4, 5, -1, -2]
    nums.sort()
    s= Solution()
    print(s.maxProd(nums))
