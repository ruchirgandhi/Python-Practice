
#n =10 so nth number is 55
#0+1=1,1+1 =2, 2+3 =5
# 0,1,1,2,3,5,8,13,21,34,55

def fib_iter(n):
    a = 0
    b = 1

    for i in range(n):
        a,b = b,a+b
        print(f"value of a is {a}")
        print(f"value of b is {b}")

    return a

print(fib_iter(10))
