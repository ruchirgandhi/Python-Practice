

from random import shuffle

List = [" ", "O", " "]
print(List)

### THIS IS VERY IMPORTANT

def shuffle_list(List):
    shuffle(List)
    return List

shuffled_list = shuffle_list(List)
print(shuffled_list)


def Guess():
    guess = ""
    while guess not in ["0","1","2"]:

        guess = input("Please Enter your number:  ")

    return int(guess)


Myguess = Guess()

def game(shuffled_list, Myguess):

    if shuffled_list[Myguess] == "O":
        print("Your guess is correct")
    else:
        print("Try again")


game(shuffled_list,Myguess)





