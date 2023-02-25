

#for example if n =0, return 4+3+2+1+0 = 10
# n + n-1 + n-2 + n-3+ ....+ 0



def sumOfInt(n):

    if n == 0:
        return 0

    else:
        return n + sumOfInt(n-1)


print(sumOfInt(4))






