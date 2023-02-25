
string = input("PLEASE ENTER WORD: ")

reverse_string = string[::-1]
print(reverse_string)


def is_palindrome(string):
	if (string[::-1] == reverse_string):
		print("word is a palindrome")
	else: 
		print("word is not a palindrome")


is_palindrome(string)


	
