"""

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].


#Two sums problem
class Solution():

    def findTwoSums(self,Nums, Target):
        d = {}
        for i in range(0,len(Nums)):
            remaining = Target- Nums[i]
            if remaining in d:
                return [d[remaining],i]
            else:
                d[Nums[i]] = i
                print(d)


s = Solution()
print(s.findTwoSums([2,4,5,10],7))

"""


class Solution():

    def twosums(self,nums, Target):
        d = {}

        for i in range(len(nums)):
            remaining = Target- nums[i]
            if remaining in d:
                return [d[remaining], i]
            else:
                d[nums[i]] = i


s = Solution()
print(s.twosums([5,1,2,1,6,3], 11))


