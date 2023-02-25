import re
from collections import Counter

class Solution:
    def count_words(self,path):
        with open(path,'r') as f:
            file = f.read()
            find_all = re.findall("[A-Za-z0-9'-]+", file)


            word_count = Counter(find_all)
            for word in word_count.most_common(1):
                print("most common word is {} and its occurance is {}".format(word[0],word[1]))



path = "cheatsheet.txt"

s = Solution()
s.count_words(path)


