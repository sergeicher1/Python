# with open("hello3.txt", "r") as work_file:
#     content_of_file = work_file.readlines()
#     line1 = content_of_file[0]
#     line2 = content_of_file[1]
#     print(line1, end="")
#     print(line2)


FILENAME = "messages.txt"
messages = list()
for i in range(4):
    message = input("Enter the string " + str(i + 1) + ": ")
    messages.append(message + "\n")

with open(FILENAME, "a") as file:
    for message in messages:
        file.write(message)

print("Reading messages from file")
with open(FILENAME, "r") as file:
    for message in file:
        print(message, end="")
