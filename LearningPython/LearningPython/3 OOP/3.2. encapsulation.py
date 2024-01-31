class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print("Invalid age!")

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name} Age: {self.__age}")


tom = Person("Tom")
tom.display_info()
tom.age = -400
print(tom.age)
tom.age = 45
tom.display_info()
