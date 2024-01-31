# for i in range(1,10, 2):
#     print(i)
#
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print("\n")

numbers = list(range(1, 10, 3))
print(numbers)
users_list = [
    ["Tom", "123"],
    ["Bob", "456"],
    ["Sam", "135"]
]

users_dict = dict(users_list)
print(users_dict)