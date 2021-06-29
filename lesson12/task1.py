# Task 2

# Create a base class named Animal with a method called talk and then create two subclasses:
# Dog and Cat, and make their own implementation of the method talk be different.
# For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.
#
# Also, create a simple generic function, which takes as input instance of a Cat or Dog classes
# and performs talk method on input parameter.

class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello, my name is {self.name}")


class Dog(Animal):
    def __init__(self, name, bark):
        Animal.__init__(self, name)
        self.bark = bark

    def talk(self):
        print(f'Dog {self.name} say {self.bark}.')


class Cat(Animal):
    def __init__(self, name, meow):
        Animal.__init__(self, name)
        self.meow = meow

    def talk(self):
        print(f'{self.meow} - {self.name} say! .')


d = Dog("Bob", "'BARK'")
c = Cat('Kitty', "'MEOW'")


def talk_animals(dog, cat):
    return Cat.talk(cat), Dog.talk(dog)


talk_animals(d, c)

# animals_list = [Dog("Bob", "'BARK'"), Cat('Kitty', "'MEOW'")]
#
# for animals in animals_list:
#     animals.talk()
