# users_list = [
#     ["Tom", "123"],
#     ["Bob", "456"],
#     ["Sam", "135"]
# ]
#
# users_dict = dict(users_list)
# print(users_dict)

users_dict = {
    "Tom": "123",
    "Bob": "456",
    "Sam": "135"
}
for key in users_dict.keys():
    print(f"key: {key}")
for value in users_dict.values():
    print(f"value: {value}")