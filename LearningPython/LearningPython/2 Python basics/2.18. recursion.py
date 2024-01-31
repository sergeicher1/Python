# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# n = 10
#
# for i in range(n):
#     print(fibonacci(i))

def factorial(n, a=1):
    if n == 0:
        return a
    else:
        return factorial(n - 1, n * a)


print(factorial(6))
