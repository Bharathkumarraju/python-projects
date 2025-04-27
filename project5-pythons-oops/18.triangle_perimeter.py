class Triangle:
    # initialize attributes
    def __init__(self, a, b, c):
        self.s1 = a
        self.s2 = b
        self.s3 = c

    # method to compute perimeter
    # Hint: you don't need to pass additional arguments to solve this problem
    def get_perimeter(self):
        perimeter = self.s1 + self.s2 + self.s3
        return perimeter

    # take three integer inputs


a = int(input("enter a"))
b = int(input("enter b"))
c = int(input("enter c"))

# create an object of Triangle
t1 = Triangle(a, b, c)

# call the get_perimeter() method using the object
result = t1.get_perimeter()

print(result)