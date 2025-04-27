"""
So adding attributes to objects is not a good practice.
Python offers a much more elegant way of defining attributes when we create objects.
For this we use special method __init__()

the __init__() is a special method, that is called automatically when an object is created.

"""

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(f"hello {self.a}, {self.b}")

test1 = Test("hi", "how are you?")

"""
__init__() is special method that is getting called when an object created.
python offers a elegant way of defining attributes when creating objects. for this we use special method called __init__()
"""