# tom = ("Tom", 24)
# print(tom)
# bob = "Bob", 23
# print(bob)
# data = ["Tom", 23, "Google", "Software"]
# tom = tuple(data)
# # print(tom)
# # print(len(tom))
# # print(tom[0])
# # tom[0] = "Bob"
# # name, age, company = tom
# # print(name)
# # print(age)
# # print(company)
# print(tom[1:3])

# def get_user():
#     name = "Tom"
#     age = 23
#     company = "Microsoft"
#     return  name, age, company
#
# user = get_user()
# print(user)

# def print_person(name, age, company):
#     print(f"Name: {name} Age: {age} Company: {company}")


tom = ("Tom", 23, "Google")
name = "Tom"
if name in tom:
    print("Name in tuple tom")
# i = 0
# while i < len(tom):
#     print(tom[i])
#     i += 1
# for i in tom:
#     print(i)
# print_person(*tom, "Microsoft")
# bob = ("Bob", 22, "Apple")
# print_person(*bob)