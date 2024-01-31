# def func(*args):
#     print(args[0])
#     print(args)
#
#
# func("Python", "C++", "Java", "C#")

# def sum(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result
#
#
# print(sum(1, 2, 3))
# print(sum(1, 2, 3, 5, 7, 8))
# print(sum(1, 2))

# def fun(**kwargs):
#     for key in kwargs:
#         print(f"{key} = {kwargs[key]}")
#
# fun(name="Tom", age= 36, company="Google")
# fun(language = "Python", version ="3.12")
# def sum(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result
#
# numbers = (1,2,3,4,5)
# print(sum(*numbers)) # Unpack

# def print_person(name, age, company):
#     print(f"Name: {name}, Age: {age}, Company: {company}")
#
#
# tom = {"name": "Tom", "age": 38, "company": "Google"}
#
# print_person(**tom)
def sum(num, num2, *nums):
    result = num + num2
    for n in nums:
        result += n
    return result


print(sum(1, 2, 3))
print(sum(1, 2, 3, 4, 5, 6))
