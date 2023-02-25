
"""
class Parenthesis(object):
    def validParen(self,s):

        if len(s)%2 !=0:
            return False

        opening = set('([{')
        print(opening)

        matches = set([('(',')'),('[',']'),('{','}')])
        print(matches)

        stack = []

        for paren in s:
            if paren in opening:
                stack.append(paren)

            else:
                if len(stack) == 0:
                    return False

                open_paren = stack.pop()
                print(open_paren,paren)

                if (open_paren,paren) not in matches:
                    return False

        return len(stack) == 0


s = Parenthesis()

print(s.validParen('{{}}[()]'))





"""


class Parenthesis():

    def helper(self,string):


        opening = set(("({["))

        matches = set([("(",")"),("{","}"),("[","]")])

        stack = []


        for paren in string:

            if paren in opening:

                stack.append(paren)

            else:

                if len(stack) == 0:
                    return False

                open_paren = stack.pop()

                if (open_paren, paren) not in matches:
                    return False

        return len(stack) ==0


s= Parenthesis()
print(s.helper("[]()[]"))
