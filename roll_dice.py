import random


repeat = True

while repeat:
	flag = input("DO YOU WANT TO ROLL A DICE?? ANSWER Y or Yes:     ")
	if flag == "Y" or flag =="Yes":
		number = random.randint(1,6)
		print(number)
	else:
		repeat= False
			
	



