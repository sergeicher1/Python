# try:
#     number1 = int(input("Enter number: "))
#     number2 = int(input("Enter number: "))
#     if number2 == 0:
#         raise Exception("The second number must not be 0")
#     print("Result: ", number1 / number2)
# except ValueError:
#     print("Incorrect data entered")
# except Exception as message:
#     print(message)
#
# print("End of program")
class PersonAgeException(Exception):
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return f"Invalid value: {self.age}. Age must be between {self.minage} and {self.maxage}"


class Person:
    def __init__(self, name, age):
        self.__name = name
        minage, maxage = 1, 110
        if minage < age < maxage:
            self.__age = age
        else:
            raise PersonAgeException(age, minage, maxage)

    def display_info(self):
        print(f"Name: {self.__name} Age: {self.__age}")


try:
    tom = Person("Tom", 37)
    tom.display_info()
    bob = Person("Bob", -20)
    bob.display_info()
except PersonAgeException as message:
    print(message)
