class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        print(f"the student name is: {self.name}\nthe score is {self.score}")
    def pass_fail(self):
        if self.score >= 40:
            return True
        else:
            return False

student1 = Student("HundanaHara", 99)
result = student1.pass_fail()
print(f"is the student {student1.name} pass?",result)
print("")
student2 = Student("Prayash", 34)
result = student2.pass_fail()
print(f"is the student {student2.name} pass?", result)