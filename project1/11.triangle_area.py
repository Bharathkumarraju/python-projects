# Get three sides of a triangle
a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

# Compute the semiperimeter
s = (a + b + c)/2
c = (s * (s-a) * (s-b) * (s-c) )
area = c ** (1/2)


# Compute area and print it
print(area)