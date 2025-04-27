############################# Explanation ##############################
""""
So when we define methods, We must use self as the first argument.
It is because, we are calling the method using the object student1.check_pass_fail().
This student1 object is automatically passed to the check_pass_fail() method. and the self argument will be this object.

We must always use self as the first argument in the function definition. This self takes the value of the object calling it.
"""
# We must always use self as the first argument in the function definition. This self takes the value of the object calling it.

class Student:
    def check_pass_fail(self):
        if self.score >= 40:
            return True
        else:
            return False

# create objects
student1 = Student()
student1.name = 'Bharath'
student1.score = 99

did_pass = student1.check_pass_fail()
print(f"Is the student1 i.e. {student1.name} Passed?", did_pass)


student2 = Student()
student2.name = "Roopa"
student2.score = 39

did_pass = student2.check_pass_fail()
print(f"Is the student2 i.e. {student2.name} Passed?", did_pass)