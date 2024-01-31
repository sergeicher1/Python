try:
    number1 = int(input("Enter first number: "))
except ValueError as e:
    print("Exception details: ", e)

print("End of program")
