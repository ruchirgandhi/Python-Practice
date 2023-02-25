Input= ["i", "love", "leetcode", "i", "love", "coding"]

k = 3

from collections import Counter

class Solution:
    def topK(self, Input, k):
        Input.sort()
        count = Counter(Input).most_common(k)
        list = []
        for key, val in count:
            list.append(key)
        return list


s = Solution()
print(s.topK(Input,k))





