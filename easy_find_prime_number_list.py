


def find_prime(num):
	for i in range(2,num):
		if num % i ==0:
			print("Its NOT a prime number")
			break
	else:
		print("IT is a prime number")

num = int(input("Please enter a number:   "))
find_prime(num)

