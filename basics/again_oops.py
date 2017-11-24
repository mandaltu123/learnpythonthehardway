class Dog:
    def __init__(self, color, breed, name):
        self.color = color
        self.breed = breed
        self.name = name


    def speak(self):
        print("freakin dogs bark")


    def guard(self):
        print("well some dogs guard our houses too")


tommy = Dog("brown", "siberian husky", "tommy")
tommy.speak()
tommy.guard()
print("{}'s color is {} and it is a {}".format(tommy.name, tommy.color, tommy.breed))