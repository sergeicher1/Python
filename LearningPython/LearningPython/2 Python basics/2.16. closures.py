# def outer():
#     n = 5
#
#     def inner():
#         nonlocal n
#         n += 1
#         print(n)
#
#     return inner
#
# fn = outer()
# fn()
# fn()
# fn()

def multiply(n): return lambda m: n * m


fn = multiply(5)
print(fn(5))
