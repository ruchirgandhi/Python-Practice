
nums = [1,2,3,4,5,1,2,3,4,4,5,6,7,8]


class Solution:
    def secLargest(self, nums):
        nums = set(nums)
        nums.remove(max(nums))
        return max(nums)


if __name__ == "__main__":
    s= Solution()
    print(s.secLargest(nums))
