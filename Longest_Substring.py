string = "aaBBccDD"


class Solution:
    def longest(self,string):
        max_len = 0
        sub = ''
        for l in string:
            if l in sub:
                sub = sub[sub.find(l)+1:]
            sub += l
            if len(sub) > max_len:
                max_len = len(sub)
        return max_len


s = Solution()
print(s.longest(string))