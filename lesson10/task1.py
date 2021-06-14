# Task 1
# Make a class called Person. Make the __init__() method take firstname, lastname, age
# as parameters and add them as attributes.
# Make another method called talk()
# which makes prints a greeting from the person containing

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old")


p1 = Person("Tim", "Cook", 60)
p1.talk()
