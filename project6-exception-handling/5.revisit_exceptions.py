try:
    a=  int(input("Enter first number: "))
    b = int(input("enter second number: "))

    division  = a/b
    print("the division is: ", division)
except Exception as e:
    print(f" the exception is this: {e} ")