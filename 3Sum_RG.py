nums = [-1,0,1,2,-1,-4]

class Solution:
    def threesum(self,nums):
        result = []
        nums.sort()
        length= len(nums)

        for i in range(length-2):
            if nums[i] >0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, length-1
            
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total <0:
                    l += 1
                elif total >0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l <r and nums[l] == nums[l+1]:
                        l +=1
                    while l <r and nums[r] == nums[r-1]:
                        r -=1
                    l +=1
                    r -=1
        return result

s = Solution()
print(s.threesum(nums))



