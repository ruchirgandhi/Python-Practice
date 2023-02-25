
def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            print(num, "is not a prime")
            break
    else:
        print(num, "is a prime")

print(is_prime(6))


