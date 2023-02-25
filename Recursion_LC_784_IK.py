
"""

784. Letter Case Permutation

Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.



Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]

"""

class Solution():

    def permutation(self,S):

        results = []


        def helper(S, i, slate):

            if i ==len(S):
                results.append(slate)

            else:

                if S[i].isdigit():
                    helper(S,i+1, slate+ S[i])

                else:
                    helper(S,i+1, slate+ S[i].upper())
                    helper(S,i+1, slate + S[i].lower())

        helper(S,0,"")

        return results
    
S= Solution()
print(S.permutation("a1b2"))


