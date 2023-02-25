

import heapq

class Solution:
    def sorting(self,nums):

        heapq.heapify(nums)
        result = []

        while len(nums)!=0:
            result.append(heapq.heappop(nums))
        return result


s = Solution()
print(s.sorting([3,2,1]))
