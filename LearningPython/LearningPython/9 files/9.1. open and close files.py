# try:
#     my_file = open("hello2.txt", "w")
#     try:
#         my_file.write("Hello zero-to-hero.dev")
#     except Exception as message:
#         print(message)
#     finally:
#         my_file.close()
# except Exception as message:
#     print(message)


with open("hello2.txt", "w") as file:
    file.write("Come a zero to Become the HERO!")
