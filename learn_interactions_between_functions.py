
from random import shuffle


def player_guess():
    guess = ""
    while guess not in ["0","1" ,"2"]:
        guess = input("Please enter number 0,1 or 2:")
    return int(guess)

def shuffle_game(mylist):
    shuffle(mylist)
    return mylist


def check_guess(mylist, guess):
    if mylist[guess] == "O":
        print("Correct !!!")
        print(mylist)
    else:
        print("Wrong Guess !!")
        print(mylist)



# Initial list

mylist = [" ", "O", " "]

mixedup_list = shuffle_game(mylist)

guess = player_guess()

check_guess(mixedup_list,guess)