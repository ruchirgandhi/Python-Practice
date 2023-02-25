#must watch video of Omcar in practice session at 3 hrs:15 mins and onwards, he will explain swap

class Solution(object):
    def perm(self, nums):
        results = []

        def helper(S,i, slate): # base case
            if i == len(S):
                results.append(slate[:])
                return

            else: #internal node worker
                if





