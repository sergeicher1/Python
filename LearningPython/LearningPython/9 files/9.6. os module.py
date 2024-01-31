import os

if os.path.exists("NEW HELLO.txt"):
    os.remove("NEW HELLO.txt")
else:
    print("The file does not exists!")
