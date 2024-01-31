from zipfile import ZipFile

with ZipFile("zero-to-hero.zip", "r") as file:
    content = file.read("hello.txt")
    print(content)
