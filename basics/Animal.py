"""
This is a weird concept, but to be very honest, you only have to worry about it when you make new classes and when you
use a class. I will show you two tricks to help you figure out whether something is a class or object.
First, you need to learn two catch phrases: “is-a” and “has-a.” You use the phrase is-a when you talk about objects and
classes being related to each other by a class relationship. You use has-a when you talk about objects and classes that
are related only because they reference each other.
Now, go through this piece of code and replace each ## ?? comment with a replacement com- ment that says whether the
next line represents an is-a or a has-a relationship and what that relationship is. In the beginning of the code, I’ve
laid out a few examples, so you just have to write the remaining ones.
Remember, is-a is the relationship between Fish and Salmon, while has-a is the relationship between Salmon and Gills.
"""


class Animal(object):
    pass

# ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name
        self.pet = None


## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ??
        self.name = name
        self.salary = salary


class Fish(object):
    pass


class Salmon(Fish):
    pass


class Halbout(Fish):
    pass



## Rover is a dog

dover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Mary")
mary.pet = satan
james = Person("James")
james.pet = dover

print("{}'s pet is {}".format(mary.name, mary.pet.name))
print("{}'s pet is {}".format(james.name, james.pet.name))
