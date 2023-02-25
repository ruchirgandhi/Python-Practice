

import heapq

class Solution(object):
    def sortArray(self,nums):
        heapq.heapify(nums)
        result = []
        while len(nums) != 0:
            result.append(heapq.heappop(nums))
        return result

s = Solution()
print(s.sortArray([3,2,1]))
