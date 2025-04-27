from sqlalchemy.dialects.mssql import dialect


def greet(messgae="how are you?"):
    print(messgae)

greet("hellooooo!")
print("")
greet()


def display(symbol = '*', number = 5):
    print(f"the symbol is: {symbol}")
    print(f"the number is: {number}")

print("when no arguments are passed!")
display()

print("When one argument is passed!")
display(symbol='#')

print("When both the arguments are passed!")
display(symbol='*', number=18)
