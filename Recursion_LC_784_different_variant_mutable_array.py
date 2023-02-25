
###input is MUTABLE CHAR ARRAY

class Solution():

    def permutation(self,S):

        results = []


        def helper(S, i, slate):

            if i == len(S):
                results.append("".join(slate))
                return

            else:

                if S[i].isdigit():

                    slate.append(S[i])
                    helper(S,i+1,slate)
                    slate.pop()

                else:
                    slate.append(S[i].lower())
                    helper(S,i+1,slate)
                    slate.pop()

                    slate.append(S[i].upper())
                    helper(S,i+1,slate)
                    slate.pop()


        helper(S,0, [])
        return results

