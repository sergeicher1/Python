from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int = 18
    def say_hello(self):
        print(f"{self.name} says hello")

tom = Person("Tom", 24)
print(f"Name: {tom.name} Age: {tom.age}")
bob = Person("Bob")
print(f"Name: {bob.name} Age: {bob.age}")
tom.say_hello()











# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"Person name ={self.name!r}, age = {self.age!r}"
#
#     def __eq__(self, other):
#         if other.__class__ is self.__class__:
#             return (self.name, self.age) == (other.name, other.age)
#         return NotImplemented
