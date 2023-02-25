import sys

def doubler(number):
    result=number *2
    return result



if __name__ == '__main__':
    try:
	input=float(sys.argv[1])
    except (IndexError, ValueError) as e:
	print("YOU MUST PROVIDE NUMBER")
	sys.exit(1)



    answer = doubler(input)
    print(answer)
	


	
