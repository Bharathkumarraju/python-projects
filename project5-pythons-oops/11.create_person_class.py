class Person:
    def __init__(self):
        pass
    def greet(self, mesage):
        self.message = mesage
        print(self.message)

greeting = str(input("enter a greeting"))
person1 = Person()
person1.greet(greeting)