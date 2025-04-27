class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def check_pass_fail(self):
        if self.score >= 40:
            return True
        else:
            return False

student1 = Student('bharath', 99)
did_pass = student1.check_pass_fail()
print(f"the student {student1.name} is passed?", did_pass)

"""
student1 = Student('bharath', 99)
So when the student1 object is created, the __init__() method is automatically called. Inside this method,
self takes the value of object - student1
    the name argument will be bharath
    the score argument will be 99
"""

student2 = Student("roopa", 39)
did_pass = student2.check_pass_fail()
print(f"the student {student2.name} is passed?", did_pass)
