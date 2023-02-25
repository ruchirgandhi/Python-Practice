
"""

try:
    for i in ["a","b","c"]:
        print(i**2)
except TypeError:
    print("Not a Valid output")

finally:
    print("I always run")





try:
    x,y = 5,0
    z= x/y
    print(z)
except ZeroDivisionError:
    print("not a valid output")

finally:
    print("i always run")


"""
while True:

    try:
        result = int(input("Please Enter your number :"))
        z= result**2

    except:
        print("Not a valid function")
        continue

    else:
        print(z)
        break

    finally:
        print("I always run")