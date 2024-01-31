# name = "Tom"
# some_text = f"Hello, {name}"
# print(some_text)
# name = "Bob"
# age = 24
# info = f"Name: {name} Age: {age}"
# print(info)

# name = "Tom"
# some_text = "Hello, {0}{0}{0}".format("Tom")
# print(some_text)

# welcome = "Hello {:s}"
# name = "Tom"
# formatted_welcome = welcome.format(name)
# print(formatted_welcome)
# source = "{:,d} chars"
# number = 5000
# target = source.format(number)
# print(target)
# num = 5000.234252352
# source = "{:,.2f} chars".format(num)
# print(source)
# num  = 23.564646456
# print(f"{num:10.2f}")
# num = 12345.54321
# print(f"{num:e}")
info = "Name: %s \t Age: %d" % ("Tom", 24)
print(info)