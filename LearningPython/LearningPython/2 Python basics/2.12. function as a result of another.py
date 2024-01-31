# def say_hello():
#     print("Hello")
#
#
# def say_goodbye():
#     print("Goodbye")
#
#
# message = say_hello
# message()
# message = say_goodbye
# message()

# def do_operation(a, b, operation):
#     result = operation(a, b)
#     print(f"result = {result}")
#
#
# def sum(a, b):
#     return a + b
#
#
# def multiply(a, b):
#     return a * b
# do_operation(4,4, sum)
# do_operation(4,4, multiply)


def sum(a, b): return a + b


def substract(a, b): return a - b


def multiply(a, b): return a * b


def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return substract
    else:
        return multiply


operation = select_operation(1)
print(operation(10, 6))
operation = select_operation(2)
print(operation(10, 6))
operation = select_operation(3)
print(operation(10, 6))
