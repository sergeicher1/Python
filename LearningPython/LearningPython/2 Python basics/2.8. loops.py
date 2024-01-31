# number = 1
# while number <= 5:
#     print(f"number = {number}")  # this condition is not executed!
#     number += 1
# else:
#     print(f"number = {number}. Loop completed")
# print("The program is ended!")

# message = "hello"
# for char in message:
#     print(char, end=",")


# i = 1
# j = 1
# while i < 10:
#     while j < 10:
#         print(i * j, end="\t")
#         j += 1
#     print("\n")
#     j = 1
#     i += 1

# for c1 in "ab":
#     for c2 in "ba":
#         print(f"{c1}{c2}")

number = 0
while number < 5:
    number += 1
    if number == 3:
        continue
    print(f"number = {number}")
