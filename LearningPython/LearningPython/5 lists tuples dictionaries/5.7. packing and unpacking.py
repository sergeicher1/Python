# x,y = (1, 2)
# print(x, y)

# name, age, company = ["Tom", 32, "Google"]
# print(name, age, company)
# dictionary = {"red":"red", "blue":"blue", "green":"green"}
# r,b,g = dictionary
# print(r,b,g)

# people = [
#     ["Tom", 32, "Google"],
#     ["Bob", 25, "Microsoft"],
#     ["Sam", 40, "Apple"]
# ]
#
# for name, age, company in people:
#     print(f"Name: {name}, Age: {age}, Company: {company}")
# people = ["Tom", "Bob", "Sam"]
# for index, name in enumerate(people):
#     print(f"{index}. {name}")
#
# people = ["Tom", 32, "Google"]
# name, _, company = people
# print(name)
# print(company)
# print(_)
# num = 1
# num2 = 2
# num3 = 3
# *numbers, = num, num2, num3
# print(numbers)

nums = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]
nums3 = [*nums, *nums2]
print(nums3)