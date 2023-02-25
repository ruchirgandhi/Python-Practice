#784
"""
i/p
S= "a1b2"

o/p= [A1b2, a1b2,A1b2, a1B2]

it will be a permutation as order matters
"""


class Solution(object):
    def permutation(self, S):

        results= []

        def helper(S, i, slate):
            if i == len(S):
                results.append(slate)
                return

            else:
                if S[i].isdigit():
                    helper(S,i+1, slate + S[i])
                else:
                    helper(S,i+1, slate + S[i].upper())
                    helper(S,i+1, slate + S[i].lower())


        helper(S,0,"")
        return results
s = Solution()
print(s.permutation("a1b2"))







