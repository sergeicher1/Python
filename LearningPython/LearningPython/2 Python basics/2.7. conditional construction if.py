# language = "german"
# if language == "russian":
#     print("Hello mir!")
# elif language == "german":
#     print("Hallo german!")
# else:
#     print("Hello english!")


#
# language = "english"
# daytime = "morning"
# if language == "english":
#     print("english")
#     if daytime == "morning":
#         print("morning")


language = "german"
daytime = "morning"
if language == "english":
    if daytime =="morning":
        print("Good morning, english!")
    else:
        print("Good evening, english!")
elif language == "german":
    if daytime == "morning":
        print("Good morning, german!")
    else:
        print("Good evening, german!")
else:
    print("Good morning!")