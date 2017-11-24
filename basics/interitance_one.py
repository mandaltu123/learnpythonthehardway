class Dog:
    def speak(self):
        print("Dog is barking")

    def guard(self):
        print("guardian of galaxy")


class ChildDog(Dog):
    def hobby(self):
        """
        Tommy has a hobby, it is programming in pyhton
        :return:  prints the hobby
        """
        print("Programming in python")


tommy = ChildDog()
print(type(tommy))
print(dir(tommy))
print(tommy.hobby())
print(isinstance(tommy, ChildDog))
tommy.speak()
tommy.guard()