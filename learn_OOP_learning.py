"""
class Dog():

    def __init__(self, breed, name, spots):
        self.breed= breed
        self.name = name
        self.spots = False

my_dog = Dog(breed="Huskie",name="Tommy", spots = False)

print(my_dog.name)
print(my_dog.spots)
print(my_dog.spots)


class Circle():

    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
        self.area = self.radius * self.radius * Circle.pi

    def get_circumference(self):

        return 2 * Circle.pi * self.radius

my_circle = Circle(radius=30)

print(my_circle.get_circumference())
print(my_circle.radius)
print(my_circle.area)




class Animal():

    def __init__(self):
        print("Animal created")

    def eat(self):
        print("i am eating")

    def who_am_i(self):
        print("zebra")


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

my_dog = Dog()
print(my_dog.eat())
print(my_dog.who_am_i())



"""

class Dog():


    def __init__(self, breed, name, spots):
        self.breed = breed
        self.spots = spots
        self.name = name

my_dog = Dog(breed="Huskie", name= "Sammy", spots="no spots")

print(my_dog.name)
print(my_dog.breed)
print(my_dog.spots)





