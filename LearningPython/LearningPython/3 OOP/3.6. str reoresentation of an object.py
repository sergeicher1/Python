class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(self)

    def __str__(self):
        return f"Name: {self.name} Age: {self.age}"


tom = Person("Tom", 25)
print(tom)
tom.display_info()
