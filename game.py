import time
import random

def waiting_game():
	number = random.randint(1,4)
	print("\nYour Timer is set to {}".format(number))

	input('----Press Enter to Begin----')
	start = time.perf_counter()
	
	input("\n...Please Enter again after {} seconds".format(number))

	elapsed = time.perf_counter() - start
	

	print(elapsed)





