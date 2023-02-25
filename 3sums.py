nums = [-1,0,1,2,-1,-4]
length = len(nums)
res = []
nums.sort()

for i in range(length-2):
    l = i +1
    r = length-1
    if nums[i] > 0: break
    if i > 0 and nums[i] == nums[i - 1]: continue
    if l < r:
        total = nums[i] + nums[l] + nums[r]

        if total < 0:
            l +=1
        elif total>0:
            r -=1
        else:
            res.append([nums[i],nums[l], nums[r]])
            while l<r and nums[l] ==nums[l+1]:
                l +=1
            while l<r and nums[r] == nums[r-1]:
                r -=1
            l+=1
            r-=1



print(res)

