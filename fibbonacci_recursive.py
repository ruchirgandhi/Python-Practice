


#n =10 so nth number is 55
#0+1=1,1+1 =2, 2+3 =5
# 0,1,1,2,3,5,8,13,21,34,55

def fib_rec(n):

    #base case
    if n == 0 or n == 1:
        return n
    # recursive
    else:
        return fib_rec(n-1) + fib_rec(n-2)


print(fib_rec(10))

