from traceback import print_tb


class Person:
    def __init__(self):
        self.name = str(input("Enter a name: "))
        self.age = int(input("Enter your age: "))
    def display_info(self):
        print(f"The name is: {self.name}")
        print(f"the age is: {self.age}")

p1 = Person()
p1.display_info()

p2 = Person()
p2.display_info()
