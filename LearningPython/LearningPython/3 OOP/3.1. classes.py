# class Person:
#     def say(self, message):
#         print(message)
#     def say_hello(self):
#         self.say("Hello!")
#
# tom = Person()
# tom.say_hello()

# class Person:
#     # constructor
#     def __init__(self):
#         print("The object is created now!")
#
#     def say_hello(self):
#         print("Hello!")
#
# tom = Person()
# tom.say_hello()


class Person:
    def __init__(self, name):
        self.name = name
        self.age = 1

    def display_info(self):
        print(f"Name: {self.name} Age: {self.age}")


# First object created
tom = Person("Tom")
tom.age = 25
tom.display_info()
# Second object created
bob = Person("Bob")
bob.age = 44
bob.display_info()
# Third object created
sam = Person("Sam")
sam.age = 33
sam.display_info()
