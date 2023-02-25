
#two.py

import learn_name_main

print("TOP LEVEL in TWO.py")

learn_name_main.eat()


if __name__ == "__main__":
    print("TWO.py is being run directly")
else:
    print("two.py has been imported")



