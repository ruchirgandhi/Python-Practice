input = [[1,3],[2,6],[8,10],[15,19]]

class Solution:
    def mergeSol(self,input):
        input.sort(key = lambda x : x[0])

        merged = []
        for i in input:
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], i[1])
        return merged

s = Solution()
print(s.mergeSol(input))






