# def message():
#     print("hello")

# lambda
# message = lambda: print("hello")
# message()

# square = lambda n: n * n
# print(square(4))
# print(square(10))
#
# sum = lambda a,b: a+ b
# print(sum(4,5))
def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")


do_operation(5, 4, lambda a, b: a + b)
do_operation(5, 4, lambda a, b: a * b)
