

def twoSum(nums, target):

    i = 0
    j = len(nums)-1

    while i < j:
        if nums[i] + nums[j] == target:
            return [i+1,j+1]

        elif nums[i] + nums[j] > target:
            j -=1
        else:
            i+=1


print(twoSum((2,7,8,15),15))

