intervals = [[5,9],[3,6],[7,10],[1,2]]


class Solution:
    def merge(self,intervals):
        intervals.sort(key= lambda x: x[0])
        print(intervals)

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1],interval[1])
        return merged

s = Solution()
print(s.merge(intervals))

