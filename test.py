result = []

def find_prime_number(In):
	divisor = 2
	while(divisor <= In):
		if (In % divisor) ==0:
			result.append(divisor)
			print(result)
			In = In/divisor
		else:
			divisor += 1
	return result
			

In = int(input("Please Enter Number: "))
find_prime_number(In)

		
