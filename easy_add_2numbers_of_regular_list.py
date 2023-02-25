
l1= [1,2,3]
l2 = [4,5,6]





"""

class Solution:
    def addTwoNumbers(self, l1, l2):
        list = []
        for i, j in zip(l1,l2):
            list.append(i+j)
        return list

s = Solution()
print(s.addTwoNumbers(l1,l2))


"""

class Solution:

    def add2(self, l1, l2):
        res = []
        for i in range(0,len(l1)):
            new = l1[i] + l2[i]
            res.append(new)
        return res


s = Solution()
print(s.add2(l1,l2))