# def print_hello(language):
#     match language:
#         case "russian":
#             print("Privet")
#         case "english" | "british" | "american":
#             print("Hello")
#         case "german":
#             print("Hallo")
#         case _:
#             print("Undefined language")
#
# print_hello("american")
# # print_hello("russian")
# # print_hello("german")
# # print_hello("spanish")
def operation(a, b, code):
    match code:
        case 1:
            return a + b
        case 2:
            return a - b
        case 3:
            return a * b
        case _:
            return 0


print(operation(10, 5, 1))
print(operation(10, 5, 2))
print(operation(10, 5, 3))
print(operation(10, 5, 6))
