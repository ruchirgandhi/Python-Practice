
class Solution(object):
    def subsets(self,nums):

        results = []

        def helper(S, i , slate):

            if i == len(S):
                return results.append(slate[:])
            else:
                #exclude
                helper(S,i+1,slate)
                #include
                slate.append(S[i])
                helper(S,i+1,slate)
                slate.pop()

        helper(nums,0,[])

        return results

s= Solution()
print(s.subsets(nums=[1,2,3]))






























