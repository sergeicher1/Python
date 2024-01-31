class Person:
    __match_args__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


def print_person(person):
    match person:
        case Person("Tom", 37):
            print("Default Person")
        case Person(name, 37):
            print(f"Name: {name}")
        case Person("Tom", age):
            print(f"Age: {age}")
        case Person(name, age):
            print(f"Name: {name} Age: {age}")


print_person(Person("Tom", 37))
print_person(Person("Tom", 22))
print_person(Person("Sam", 37))
print_person(Person("Bob", 41))
