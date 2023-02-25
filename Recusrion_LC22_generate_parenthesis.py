


class Solution():
    def gererateParenthesis(self,n):
        result = []

        def helper(self, numleft, numright, slate):
            if numleft > numright:
                return

            #Base Case
            if numleft ==0 and numright ==0:
                result.append(slate[:])
                return

            # recursion case
            if numleft > 0:
                slate.append("(")
                helper(self, numleft-1,numright,slate)
                slate.pop()


            if numright >0:
                slate.append(")")
                helper(self,numleft,numright-1,slate)
                slate.pop()

        helper(self,n,n,[])
        return result

s = Solution()
print(s.gererateParenthesis(3))