class Solution:
    def longestPalindrome(self, s):
        maximum = ""
        temp = ""
        for i in range(len(s)):
            for j in range(i+len(maximum),len(s)+1):
                fw = s[i:j]
                bw = fw[::-1]
                if fw == bw:
                    temp = fw
                    if len(temp) > len(maximum):
                        maximum = temp
        return maximum