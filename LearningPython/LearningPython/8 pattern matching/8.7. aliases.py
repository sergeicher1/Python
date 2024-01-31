class Person:
    __match_args__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


def check(person):
    match person:
        case (Person() as husband, Person() as wife):
            print(f"Husband. Name: {husband.name} Age: {husband.age}")
            print(f"Wife. Name: {wife.name} Age: {wife.age}")
        case _:
            print("Undefined!")


check((Person("Tom", 37), Person("Alice", 33)))
