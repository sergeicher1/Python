# def SayHello(name):
#     print(f"Hello, ", name)
#
# SayHello("Tom")
# SayHello("Bob")


# def PrintPerson(name="Tom", age=25):
#     print(f"Name: ", name)
#     print(f"Age: ", age)
#
#
# # PrintPerson()
# # PrintPerson("Sam")
# # PrintPerson("Bob", 40)
# PrintPerson(age=20, name="Alice")


def sum(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(f"sum = {result}")


sum(1, 2, 3, 4, 5)
sum(1, 2, 3)
