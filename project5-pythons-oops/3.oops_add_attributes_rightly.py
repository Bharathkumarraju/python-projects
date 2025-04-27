class Student:
    def check_pass_fail(self):
        if self.score >= 40:
            return True
        else:
            return False

student1 = Student()
student1.name = "hundanahara"
student1.score = 99

did_pass = student1.check_pass_fail()
print(f"the student {student1.name} is passed?",did_pass)

"""
So adding attributes to objects is not a good practice.
Python offers a much more elegant way of defining attributes when we create objects.
For this we use special method __init__()

the __init__() is a special method, that is called automatically when an object is created.

"""

class Test:
    def __init__(self):
        print("Hello, How are you .. I am __init__ displaying the text!")

test1 = Test()
test2 = Test()
