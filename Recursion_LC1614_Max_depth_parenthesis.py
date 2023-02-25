



class Solution():

    def depth(self, text):

        current_max = 0
        max = 0

        for i in range(len(text)):

            if text[i] == "(":

                current_max += 1

                if current_max >0:
                    max = current_max

            elif text[i] == ")":

                if current_max>0:
                    current_max -=1

                else:
                    return -1
        if current_max != 0:
            return -1

        return max


s = Solution()
print(s.depth("()((()))()()"))
