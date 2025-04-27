class Student:
    def __init__(self, name, score):
        self.i = name
        self.j = score
        print(f"the name is {self.i}\nthe score is {self.j}")
    def pass_fail(self):
        if self.j >=40:
            return True
        else:
            return False

student1 = Student("prayash", 100)
result = student1.pass_fail()
print(f"is the student {student1.i} pass?",result)
print(f"\n")
student2 = Student("hundanahara", 98)
res = student2.pass_fail()
print(f"is the student {student2.i} pass?",res)

