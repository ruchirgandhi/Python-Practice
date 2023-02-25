



class Solution:
    def maxProd(self,nums):
        nums.sort()
        print(nums)
        return max(nums[-1] * nums[-2] *nums[-3], nums[-1]* nums[0]*nums[1])

if __name__ == "__main__":

    nums = [10, 3, 5, 6, 20]

    nums = [-16, 2, 3, 4, 4, 15]

    s = Solution()
    print(s.maxProd(nums))
