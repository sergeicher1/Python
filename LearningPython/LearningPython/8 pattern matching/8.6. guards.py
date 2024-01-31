class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def check(person):
    match person:
        case Person(name=name, age=age) if age < 18:
            print(f"{name}, access denied")
        case Person(name=name, age=age) if age < 22:
            print(f"{name}, access limited")
        case Person(name=name):
            print(f"{name}, welcome!")


check(Person("Tom", 34))
check(Person("Sam", 15))
check(Person("Bob", 20))
