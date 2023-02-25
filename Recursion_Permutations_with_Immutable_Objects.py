class Solution:
    def permute(self, nums):
        result = []
        def helper(slate,S):
            if len(S) ==0:
                result.append(slate[:])
                return
            else:
                for i in range(0,len(S)):
                    helper(slate + S[i], S[:i]+ S[i+1:])
        helper([], nums)
        return result
s= Solution()
print(s.permute(nums= ([1],[4],[2],[3])))


