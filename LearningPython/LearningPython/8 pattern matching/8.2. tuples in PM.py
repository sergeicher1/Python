# def print_data(user):
#     match user:
#         case ("Tomy", 37) | ("Sam", 25):
#             print("default user")
#
#
# print_data(("Tomy", 37))
# print_data(("Sam", 25))

def print_data(user):
    match user:
        case ("Tom", 37, *rest):
            print(f"Rest : {rest}")
        case(name, age, *rest):
            print(f"{name} {age}: {rest}")


print_data(("Tom", 37))
print_data(("Tom", 37, "Google"))
print_data(("Tom", 37, "Google", "English"))

