class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines.")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")

class Quadrilateral(Polygon):
    def display_info(self):
        print('A quadrilateral is a polygon with 4 edges.')

        # call the display_info() method of baseclass-i.e. Polygon
        super().display_info()

# p1 = Polygon([3, 4, 5])
# p1.display_info()
# perimeter = p1.get_perimeter()
# print(f'Perimeter: {perimeter}')

t1 = Triangle([10, 20, 30])

perimeter = t1.get_perimeter()
print(f"perimeter is: ",perimeter)

t1.display_info()
print()

q1 = Quadrilateral([1, 2, 3, 4])
perimeter = q1.get_perimeter()
print(f"perimeter of quadrilateral: ",perimeter)

q1.display_info()

