# def get_message():
#     return "Hello zero-to-hero.dev"
#
#
# message = get_message()
# print(message)


# def double(number):
#     return 2 * number
#
#
# result = double(4)
# print(result)
#
#
# def sum_numbers(a, b):
#     return a + b
#
#
# print(sum_numbers(4, 6))


def PrintPerson(name, age):
    if age > 120 or age < 1:
        print("Invalid age")
        return
    print(f"Name: {name}, Age: {age}")


PrintPerson("Tom", 22)
PrintPerson("Bob", -20)
