"""

**kwargs
It's also possible to pass a variable number of keyword arguments in Python.
To accept these arguments in the function definition, use ** before the argument name.

"""

def print_info(**person):
    print(person)


print_info()
print_info(name = "bharath", age = 37, location = "Singapore")
print_info(name= "Sam Altman", age=45, location = "california")



def greet(**args):
    print(args)

formal = input("enter formal greetings: ")
informal = input("Enter informal greetings: ")
greet(formal = formal, informal = informal)

