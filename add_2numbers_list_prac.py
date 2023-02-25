

l1 = [4,5,6]
l2 = [3,2,1]


class Solution:
    def addTwoNumbers(self,l1,l2):
        list = []
        for i,j in zip(l1,l2):
            list.append(sorted(l1+l2))
            return list

s = Solution()
print(s.addTwoNumbers(l1,l2))

