# name = "Alice"
#
#
# def say_hi():
#     global name
#     name = "Tom"
#     print("hello, ", name)
#
#
# def say_bye():
#     print("bye, ", name)
#
#
# say_hi()
# say_bye()

def outer():
    n = 5

    def inner():
        nonlocal n
        n = 25
        print(n)

    inner()
    print(n)


outer()
