# string = "5"
# number = int(string)
# print(number)
# string2 = "hello"
# number2 = int(string2)
# print(number2)


try:
    number = int(input("Enter number: "))
    print("Entered number: ", number)
except:
    print("Conversion failed")

finally:
    print("The try block has completed")
print("End of program")
