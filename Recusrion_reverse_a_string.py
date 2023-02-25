

# reverse a string using recursion, do NOT USE s[::-1]


def reverse(s):

    #base case
    if len(s) <=1:
        return s

    else:
        return reverse(s[1:]) + s[0]


print(reverse("abc"))

